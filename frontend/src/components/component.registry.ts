import { registerComponent } from "../services/component-registry.service";
import Button from "./Button/button.component";
import Textfield from "./Textfield/textfield.component";

registerComponent({
  name: "Button",
  description: "A basic button component.",
  component: Button,
  defaultProps: { label: "Click Me" },
  variants: ['primary', 'secondary', 'warn']
});

registerComponent({
  name: "Textfield",
  description: "A basic textfield component.",
  component: Textfield,
  defaultProps: { label: "Email" },
  variants: ['outline', 'secondary', 'warn']
});