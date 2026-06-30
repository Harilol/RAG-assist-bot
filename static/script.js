async function sendMessage() {

    const input = document.getElementById("query");
    const chat = document.getElementById("chat");

    const question = input.value.trim();

    if (question === "") return;

    // User bubble
    chat.innerHTML += `
        <div class="user-message">
            ${question}
        </div>
    `;

    input.value = "";

    // Assistant bubble
    const ai = document.createElement("div");
    ai.className = "assistant-message";
    chat.appendChild(ai);

    chat.scrollTop = chat.scrollHeight;

    // Thinking animation
    let dots = 0;

    const loading = setInterval(() => {
        dots = (dots + 1) % 4;
        ai.innerHTML = "Thinking" + ".".repeat(dots);
    }, 300);

    try {

        const response = await fetch(`/chat?query=${encodeURIComponent(question)}`);

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        let first = true;
        let fullText = "";

        while (true) {

            const { done, value } = await reader.read();

            if (done) break;

            if (first) {
                clearInterval(loading);
                ai.innerHTML = "";
                first = false;
            }

            const chunk = decoder.decode(value);

            fullText += chunk;

            ai.innerHTML = marked.parse(fullText);

            chat.scrollTop = chat.scrollHeight;
        }

        // Copy button
        const copy = document.createElement("button");

        copy.className = "copy-btn";
        copy.innerText = "Copy";

        copy.onclick = () => {

            navigator.clipboard.writeText(fullText);

            copy.innerText = "Copied!";

            setTimeout(() => {
                copy.innerText = "Copy";
            }, 1500);

        };

        ai.appendChild(copy);

    } catch (err) {

        clearInterval(loading);

        ai.innerHTML = "❌ Something went wrong.";

        console.error(err);

    }

    chat.scrollTop = chat.scrollHeight;

}


// ENTER TO SEND

document.getElementById("query").addEventListener("keydown", function (e) {

    if (e.key === "Enter") {
        sendMessage();
    }

});


// PDF UPLOAD

document.getElementById("pdf").addEventListener("change", uploadPDF);

async function uploadPDF() {

    const file = document.getElementById("pdf").files[0];

    if (!file) return;

    const form = new FormData();

    form.append("file", file);

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: form
        });

        const data = await response.json();

        alert(data.message);

    } catch (err) {

        alert("Upload failed.");

        console.error(err);

    }

}