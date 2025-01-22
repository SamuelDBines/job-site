import { registerComponent } from "../services/component-registry.service";
import Button from "./Button/button.component";

registerComponent({
  name: "Button",
  description: "A basic button component.",
  component: Button,
  defaultProps: { label: "Click Me" },
  variants: ['primary', 'secondary', 'warn']
});