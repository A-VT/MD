document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('inputTextForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the form from submitting via browser

        // Get the form data
        const formData = new FormData(form);

        // Reference to textResponseDiv
        const textResponseDiv = document.querySelector('.textResponse');

        // Show loading message or indication
        textResponseDiv.innerHTML = '<p>Loading...</p>';

        // Make a POST request using fetch API
        fetch('/handleText', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())  // Expect a JSON response
        .then(data => {
            if (data.status === 'success') {
                // Clear the previous content
                textResponseDiv.innerHTML = '';

                // Iterate over the results and create HTML elements for each item
                data.results.forEach(result => {
                    const resultDiv = document.createElement('div');
                    resultDiv.classList.add('result');

                    // Create and append elements for each key in the result
                    const title = document.createElement('h3');
                    title.textContent = result.title;
                    resultDiv.appendChild(title);

                    const company = document.createElement('p');
                    company.textContent = `Company: ${result.company}`;
                    resultDiv.appendChild(company);

                    const date = document.createElement('p');
                    date.textContent = `Date: ${result.date}`;
                    resultDiv.appendChild(date);

                    const description = document.createElement('p');
                    description.textContent = `Description: ${result.description}`;
                    resultDiv.appendChild(description);

                    const locations = document.createElement('p');
                    locations.textContent = `Locations: ${result.locations}`;
                    resultDiv.appendChild(locations);

                    const salary = document.createElement('p');
                    salary.textContent = `Salary: ${result.salary}`;
                    resultDiv.appendChild(salary);

                    const site = document.createElement('p');
                    site.textContent = `Site: ${result.site}`;
                    resultDiv.appendChild(site);

                    const url = document.createElement('p');
                    const link = document.createElement('a');
                    link.href = result.url;
                    link.textContent = 'Job Link';
                    link.target = '_blank';
                    url.appendChild(link);
                    resultDiv.appendChild(url);

                    // Append the resultDiv to textResponseDiv
                    textResponseDiv.appendChild(resultDiv);
                });
            } else {
                textResponseDiv.innerHTML = '<p>There was an error processing your request.</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            textResponseDiv.innerHTML = '<p>There was an error processing your request.</p>';
        });
    });
});
