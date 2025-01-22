// components/Button.tsx
import React from "react";
import { ButtonProps } from '../shared/common.interfaces';
import "./button.styles.css";



const Button: React.FC<ButtonProps> = ({ label, variant = 'primary' }) => {
  return (
    <button className={`button ${variant}`}>
      {label}
    </button>
  );
};

export default Button;
