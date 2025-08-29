document.addEventListener("DOMContentLoaded", function () {
    const islBtn = document.getElementById("islBtn");
    const hindiBtn = document.getElementById("hindiBtn");

    islBtn.addEventListener("click", function () {
        showDialog("Enter ISL text:");
    });

    hindiBtn.addEventListener("click", function () {
        showLanguageOptions();
    });

    function showDialog(message) {
        let dialog = document.createElement("div");
        dialog.className = "dialog-box";
        dialog.innerHTML = `
            <p>${message}</p>
            <input type="text" placeholder="Type here...">
            <br>
            <button onclick="this.parentNode.remove()">Close</button>
        `;
        document.body.appendChild(dialog);
    }

    function showLanguageOptions() {
        let dialog = document.createElement("div");
        dialog.className = "dialog-box";
        dialog.innerHTML = `
            <p>Select Language:</p>
            <select>
                <option>Gujarati</option>
                <option>Marathi</option>
                <option>Tamil</option>
                <option>Telugu</option>
                <option>English</option>
            </select>
            <br>
            <button onclick="this.parentNode.remove()">Close</button>
        `;
        document.body.appendChild(dialog);
    }
});

const videoElement = document.getElementById("camera-feed");
const toggleButton = document.getElementById("toggle-camera");
let isCameraOn = false;

toggleButton.addEventListener("click", () => {
    if (!isCameraOn) {
        // Show the camera feed (this could be a static image or video stream URL)
        videoElement.style.display = "block";  
        toggleButton.textContent = "Stop Camera";  // Update button text
        toggleButton.style.background = "#dc3545";  // Change button color
        isCameraOn = true;
    } else {
        // Hide the camera feed
        videoElement.style.display = "none";
        toggleButton.textContent = "Start Camera";  // Update button text
        toggleButton.style.background = "#28a745";  // Change button color
        isCameraOn = false;
    }
});



async function fetchData() {
    const outputBox = document.querySelector('.output-box');
    outputBox.innerHTML = "Fetching data..."; // Show loading text

    // try {
    //     const response = await fetch('/example.txt'); // Ensure file path is correct
    //     if (!response.ok) {
    //         throw new Error(`HTTP error! Status: ${response.status}`);
    //     }
        
    //     const data = await response.text(); // Read text content
    //     outputBox.textContent = data; // Display text content
    // } catch (error) {
    //     console.error("Fetch error:", error);
    //     outputBox.innerHTML = `<span style="color: red;">Error: ${error.message}</span>`;
    // }

    fetch('/example.txt')
    .then(response => response.text())
    .then(data => {
        const d = response.text(); // Read text content
        outputBox.textContent = d; // Display text content
    })
    .catch(error => console.error('Error:', error));

}

// Ensure a server is running before fetching
setInterval(fetchData, 3000);
fetchData();

