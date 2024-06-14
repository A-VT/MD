document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("send-button");
    const inputText = document.getElementById("input-text");
    const responsesDiv = document.getElementById("responses");
    const messageServerDiv = document.getElementById("messageServer");

    sendButton.addEventListener("click", function () {
        const text = inputText.value;
        fetch('/handle_input', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        }).then(response => {
            return response.json();
        }).then(data => {
            // Clear previous entries
            responsesDiv.innerHTML = "";
            messageServerDiv.textContent = "Based on the data you gave us we found these job offers available:\n";

            // Process results through a for loop
            for (const result of data.results) {
                // Create new entry
                const newEntry = document.createElement("div");

                // Create and append title
                const title = document.createElement("h4");
                title.textContent = result['title'];
                newEntry.appendChild(title);

                // Create and append salary and type info
                const salaryInfo = document.createElement("p");
                salaryInfo.textContent = `Salary: ${result['salary']} | Currency: ${result['salary_currency_code']} | Type: ${result['salary_type']}`;
                newEntry.appendChild(salaryInfo);

                // Create and append URL
                const url = document.createElement("p");
                url.textContent = `URL: ${result['url']}`;
                newEntry.appendChild(url);

                // Create and append description
                const description = document.createElement("p");
                description.textContent = result['description'];
                newEntry.appendChild(description);

                // Create and append salary range
                const salaryRange = document.createElement("p");
                salaryRange.textContent = `Salary Min-Max: ${result['salary_min']} - ${result['salary_max']}`;
                newEntry.appendChild(salaryRange);

                // Append the new entry to the responses div
                responsesDiv.appendChild(newEntry);
            }

            // Clear input text
            inputText.value = "";
        }).catch(error => {
            console.error('Error:', error);
        });
    });
});