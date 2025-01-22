export interface HtmlCommonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'warn';
}

export interface TextfieldProps extends HtmlCommonProps {
  placeholder?: string;
  onChange?: () => void;
}

export interface ButtonProps extends HtmlCommonProps {
  onClick?: () => void;
}