# About
This code creates a simple HTTP server using Python's `http.server` module. It serves a login page that mimics a legitimate login form for a service called "ADNU CEVAS" (Ateneo Certificate Validation System). The goal of the code is to capture user credentials (email and password) submitted through the form. When the user logs in, the captured credentials are printed to the console, and the user is redirected to an external website (Google).

---

## Risk
This code functions as a potential phishing tool. The key risks include:
- **Credential Harvesting** – The code captures and logs sensitive user information (email and password) without encryption or user consent.
- **Misleading Interface** – The login page is designed to appear legitimate, which could deceive users into providing sensitive information.
- **Redirection** – After capturing credentials, the user is redirected to Google, further enhancing the illusion that the login attempt was genuine.
- **Network Exposure** – Running this server on a public IP could expose it to potential discovery and misuse by malicious actors.

---

## Code Block
- **Server Setup** `hostName = "localhost"` Sets the IP address to listen on.  `serverPort = 8443` – Defines the port number for the HTTP server.  
- **do_GET()** Handles GET requests by serving an HTML-based login page. Uses inline CSS for styling and embeds Google Fonts to mimic a professional UI.  
- **do_POST()** Handles POST requests to capture submitted login credentials. `parse_qs(post_data)` – Parses the form data to extract email and password. Logs the captured credentials using `print()` and redirects the user to Google.  
- **Main Server Loop** Keeps the server running until terminated.  

---

## Notes
- If this code were deployed in a real-world scenario, it could be classified as a phishing attack due to its deceptive nature.
- The use of plain HTTP instead of HTTPS means that data is transmitted in clear text, making it susceptible to interception.
- The server is running on a local IP (`localhost`), which limits its reach unless port forwarding or external exposure is configured.
- The CSS and UI design increase the credibility of the login page, making it more convincing as a phishing attempt.
- Captured credentials are not encrypted or stored securely, indicating poor handling of sensitive data.
