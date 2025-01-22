import React, { useState } from "react";
import { useModal } from "../components/Modal/modal.component";
import "./Login.styles.css";
import { loginUser } from "../services/auth.service";

const TestModal = () => {
  return (<>
    <h1> Some header</h1>
  </>
  );
};

const Login: React.FC = () => {
  const { toggleModal, component } = useModal({ children: <TestModal /> });
  const { toggleModal: tg, component: cp } = useModal({ children: <TestModal /> });
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    console.log("Login attempt with:", { username, password });
    loginUser({
      username,
      password
    }).then(u => alert('User logged in' + u)).catch(err => console.log(err));

    // Here, you could call an API to validate the login
    // If successful, navigate to a dashboard or another route
  };

  return (
    <div className="login-container">
      <h1 onClick={() => {
        toggleModal();
        tg();
      }}>Login</h1>
      {component}
      {cp}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter your email"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
          />
        </div>
        <button type="submit" className="login-button">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
