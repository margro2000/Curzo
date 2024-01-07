// ModulePage.js
import React from "react";
import { useParams, Link } from "react-router-dom";
import "./Module.css"; // Import the updated CSS file
import YouTube from "react-youtube";
import Navbar from "./Navbar";

const ModulePage = () => {
  const { moduleId } = useParams();
  const moduleNumber = parseInt(moduleId, 10);

  // Example video IDs (replace with your actual video IDs)
  const videoIds = ["zjkBMFhNj_g", "5sLYAQS9sWQ", "lnA9DMvHtfI"];

  const opts = {
    height: "390",
    width: "640",
    playerVars: {
      autoplay: 0,
    },
  };

  return (
    <div>
      <Navbar />
      <div className="module-container-two">
        <h2 className="h2-two">Module {moduleId}: Title</h2>
        <div className="summary">Summary / Goals of the module go here</div>
        <div className="module-links">
          <h3>YouTube Videos:</h3>
          <div className="video-container">
            {videoIds.map((videoId) => (
              <YouTube key={videoId} videoId={videoId} opts={opts} />
            ))}
          </div>
          <h3>Supplementary Text</h3>
          <p>Testing</p>
          <h3>Other Resources</h3>
        </div>
      </div>
      <div className="navigation-buttons">
        {moduleNumber > 1 && (
          <Link to={`/module/${moduleNumber - 1}`}>
            <button className="navigation-button">Previous Module</button>
          </Link>
        )}
        {moduleNumber < 6 && (
          <Link to={`/module/${moduleNumber + 1}`}>
            <button className="navigation-button">Next Module</button>
          </Link>
        )}
      </div>
    </div>
  );
};

export default ModulePage;
