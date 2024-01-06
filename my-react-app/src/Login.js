// LoginPage.js

import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Login.css"; // Import your login page styles
import Navbar from "./Navbar";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform login logic here, e.g., send a request to the server
    console.log("Username:", username);
    console.log("Password:", password);
    // Add your login logic or redirection after successful login
  };

  return (
    <div>
      <Navbar></Navbar>

      <div className="login-container">
        <h1 className="h1-login">Login</h1>
        <form onSubmit={handleSubmit}>
          <label className="label-login">
            Username:
            <input
              type="text"
              value={username}
              onChange={handleUsernameChange}
            />
          </label>
          <label className="label-login">
            Password:
            <input
              className="input-login"
              type="password"
              value={password}
              onChange={handlePasswordChange}
            />
          </label>
          <button className="button-login" type="submit">Submit</button>
        </form>
        <p className="p-login">
          Don't have an account?{" "}
          <Link to="/signup">Create Account</Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
