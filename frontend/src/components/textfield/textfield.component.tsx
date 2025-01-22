// components/Button.tsx
import React from "react";
import { TextfieldProps } from "../shared/common.interfaces";
import "./textfield.styles.css";



const Textfield: React.FC<TextfieldProps> = ({ label, variant = 'primary', placeholder }) => {
  return (<>
    <label>{label}</label>
    <input className={`${variant}`} placeholder={placeholder} />
  </>
  );
};

export default Textfield;
