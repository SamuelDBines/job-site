// components/Button.tsx
import React from "react";
import "./button.styles.css";

interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'warn';
}

const Button: React.FC<ButtonProps> = ({ label, variant = 'primary' }) => {
  return (
    <button className={`button ${variant}`}>
      {label}
    </button>
  );
};

export default Button;
