// ComponentRegistry.ts
interface ComponentInfo {
  name: string;
  description?: string;
  component: React.FC<T>;
  defaultProps?: Record<string, any>;
  variants?: string[];
}

// Registry to store components
const componentRegistry: ComponentInfo[] = [];

// Function to register components
export const registerComponent = (info: ComponentInfo) => {
  componentRegistry.push(info);
};

// Function to get all registered components
export const getComponents = () => componentRegistry;
