document.addEventListener("DOMContentLoaded", function () {
  const startButton = document.getElementById("start-btn");
  const stopButton = document.getElementById("stop-btn");
  const videoFeed = document.getElementById("video-feed");
  const fireAlert = document.getElementById("fire-alert");

  let fireDetected = false;
  let streamActive = false;
  let eventSource = null;

  // Function to update fire alert visibility
  function updateFireAlert() {
      if (fireDetected) {
          fireAlert.style.display = "block"; // Show alert
      } else {
          fireAlert.style.display = "none"; // Hide alert
      }
  }

  // Function to start video streaming and fire detection
  function startDetection() {
      if (!streamActive) {
          videoFeed.src = "/video_feed"; // Set video source
          videoFeed.style.display = "block"; // Show video

          // Start Fire Detection Updates
          eventSource = new EventSource("/fire_status");
          eventSource.onmessage = function (event) {
              fireDetected = event.data === "True"; // Update fire detection status
              updateFireAlert(); // Update alert display
          };

          streamActive = true;
      }

      // Send request to start processing
      fetch("/start")
          .then(response => response.json())
          .then(data => console.log(data.status))
          .catch(error => console.error("Error starting detection:", error));
  }

  // Function to stop video streaming
  function stopDetection() {
      if (streamActive) {
          videoFeed.src = ""; // Stop video
          videoFeed.style.display = "none"; // Hide video
          fireAlert.style.display = "none"; // Hide alert

          if (eventSource) {
              eventSource.close(); // Close event stream
              eventSource = null;
          }

          streamActive = false;
      }

      // Send request to stop processing
      fetch("/stop")
          .then(response => response.json())
          .then(data => console.log(data.status))
          .catch(error => console.error("Error stopping detection:", error));
  }

  // Attach event listeners
  startButton.addEventListener("click", startDetection);
  stopButton.addEventListener("click", stopDetection);
});
