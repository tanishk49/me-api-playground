const backendURL = "https://me-api-playground-rlj9.onrender.com";

async function loadProfiles() {
    try {
        const res = await fetch(`${backendURL}/profiles`);
        const profiles = await res.json();

        const container = document.getElementById("profiles-container");
        container.innerHTML = "";

        profiles.forEach(profile => {
            const div = document.createElement("div");
            div.className = "profile-card";
            div.innerHTML = `
                <h2>${profile.name}</h2>
                <p>Email: ${profile.email}</p>
                <p>Education: ${profile.education || "N/A"}</p>
                <p>Skills: ${profile.skills.map(s => s.name).join(", ") || "N/A"}</p>
                <p>Projects: ${profile.projects.map(p => p.title).join(", ") || "N/A"}</p>
            `;
            container.appendChild(div);
        });

    } catch (error) {
        console.error("Error fetching profiles:", error);
    }
}

loadProfiles();
