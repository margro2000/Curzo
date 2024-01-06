// Signup.js

import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Signup.css";
import Navbar from "./Navbar";

const Signup = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSignup = (e) => {
    e.preventDefault();
    // Perform signup logic here, e.g., send a request to the server
    console.log("Email:", email);
    console.log("Password:", password);
    // Add your signup logic or redirection after successful signup
  };

  return (
    <div>
      <Navbar></Navbar>

      <div className="signup-container">
        <h1 className="h1-signup">Create an Account</h1>
        <form onSubmit={handleSignup}>
          <label className="label-signup">
            Email:
            <input type="text" value={email} onChange={handleEmailChange} />
          </label>
          <label className="label-signup">
            Password:
            <input
              className="input-signup"
              type="password"
              value={password}
              onChange={handlePasswordChange}
            />
          </label>
          <button className="button-signup" type="submit">
            Sign Up
          </button>
        </form>
        <p>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </div>
    </div>
  );
};

export default Signup;
