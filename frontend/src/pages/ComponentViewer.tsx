// ComponentViewer.tsx
import React, { useState } from "react";
import { getComponents } from "../services/component-registry.service";

const ComponentViewer: React.FC = () => {
  const components = getComponents();
  const [selectedComponentIndex, setSelectedComponentIndex] = useState<number | null>(null);

  const [selectedVariant, setSelectedVariant] = useState<string>('primary');

  const selectedComponent =
    selectedComponentIndex !== null ? components[selectedComponentIndex] : null;

  const getVariant = React.useMemo(() => selectedVariant, [selectedVariant]);

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      {/* Sidebar */}
      <div style={{ width: "25%", borderRight: "1px solid #ddd", padding: "1rem" }}>
        <h3>Components</h3>
        <ul style={{ listStyle: "none", padding: 0 }}>
          {components.map((comp, index) => (
            <li
              key={index}
              onClick={() => setSelectedComponentIndex(index)}
              style={{
                cursor: "pointer",
                padding: "0.5rem",
                background: selectedComponentIndex === index ? "#f0f0f0" : "transparent",
              }}
            >
              {comp.name}
            </li>
          ))}
        </ul>
      </div>

      {/* Preview Area */}
      <div style={{ flex: 1, padding: "1rem" }}>
        {selectedComponent ? (
          <>
            <h2>{selectedComponent.name}</h2>
            {selectedComponent.description && <p>{selectedComponent.description}</p>}
            <div style={{ border: "1px solid #ddd", padding: "1rem", marginTop: "1rem" }}>
              {/* Render the selected component */}
              <selectedComponent.component {...selectedComponent.defaultProps} variant={getVariant} />
            </div>
            <div className="flex">
              {selectedComponent?.variants?.length && selectedComponent.variants.map((v: string) => {
                return <>
                  <input type="radio" name="variant" />{v}
                </>;
              })}
            </div>
          </>
        ) : (
          <p>Select a component to preview</p>
        )}
      </div>
    </div>
  );
};

export default ComponentViewer;
