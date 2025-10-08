from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BRAND X AWARA X PATHAN</title>
  <style>
    /* 🌌 Background and Layout */
    body {
      margin: 0;
      padding: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #0d0d0d, #000);
      font-family: 'Poppins', sans-serif;
      color: #fff;
      overflow: hidden;
      text-align: center;
    }

    /* 🔥 Glow Effect Circle Behind */
    .glow-bg {
      position: absolute;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(255,75,43,0.3), transparent);
      filter: blur(90px);
      animation: pulseGlow 5s infinite alternate ease-in-out;
    }
    @keyframes pulseGlow {
      from { transform: scale(1); opacity: 0.7; }
      to { transform: scale(1.2); opacity: 1; }
    }

    /* 🎥 Video Logo */
    .logo-video {
      width: 180px;
      height: 180px;
      border-radius: 50%;
      overflow: hidden;
      margin-bottom: 25px;
      box-shadow: 0 0 30px rgba(255,75,43,0.8), 0 0 50px rgba(30,144,255,0.6);
      animation: float 4s ease-in-out infinite alternate;
    }

    .logo-video video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 50%;
      display: block;
    }

    @keyframes float {
      from { transform: translateY(0); }
      to { transform: translateY(-10px); }
    }

    /* ✨ Logo Text */
    .logo {
      font-size: 28px;
      font-weight: 700;
      margin-bottom: 30px;
      background: linear-gradient(90deg, #ff4b2b, #f9d423, #1e90ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: 3px;
      text-transform: uppercase;
      text-shadow: 0 0 10px rgba(255,255,255,0.4);
      animation: glowText 3s infinite alternate;
    }

    @keyframes glowText {
      from { text-shadow: 0 0 15px #ff4b2b; }
      to { text-shadow: 0 0 30px #1e90ff; }
    }

    /* ⏳ Loader Rings */
    .loader {
      position: relative;
      width: 60px;
      height: 60px;
      margin-bottom: 15px;
    }

    .ring {
      width: 100%;
      height: 100%;
      border: 4px solid transparent;
      border-top: 4px solid #ff4b2b;
      border-radius: 50%;
      position: absolute;
      top: 0;
      left: 0;
      animation: spin 1.5s linear infinite;
      box-shadow: 0 0 6px #ff4b2b;
    }
    .ring:nth-child(2) {
      border-top-color: #1e90ff;
      animation-delay: 0.3s;
      box-shadow: 0 0 6px #1e90ff;
    }
    .ring:nth-child(3) {
      border-top-color: #f9d423;
      animation-delay: 0.6s;
      box-shadow: 0 0 6px #f9d423;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    /* 🔢 Counter */
    #counter {
      font-size: 36px;
      font-weight: bold;
      margin-top: 10px;
      animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
      from { color: #f9d423; text-shadow: 0 0 10px #ff4b2b; }
      to { color: #1e90ff; text-shadow: 0 0 20px #f9d423; }
    }

    /* 🛰 Status */
    #status {
      margin-top: 12px;
      font-size: 16px;
      color: #ccc;
      animation: fade 2s infinite alternate;
    }
    @keyframes fade {
      from { opacity: 0.6; }
      to { opacity: 1; }
    }
  </style>
</head>
<body>
  <div class="glow-bg"></div>

  <div class="logo-video">
    <video autoplay muted loop playsinline poster="https://raw.githubusercontent.com/hassanrajput7626/Paid-app/main/IMG-20251006-WA0262.jpg">
      <source src="https://raw.githubusercontent.com/hassanrajput7626/Paid-app/main/video.mp4" type="video/mp4">
    </video>
  </div>

  <div class="logo">BRAND X AWARA X PATHAN</div>

  <div class="loader">
    <div class="ring"></div>
    <div class="ring"></div>
    <div class="ring"></div>
  </div>

  <div id="counter">3</div>
  <div id="status">Checking Internet Connection...</div>

  <script>
    let seconds = 3;
    const counter = document.getElementById("counter");
    const status = document.getElementById("status");

    const countdown = setInterval(() => {
      seconds--;
      counter.textContent = seconds;
      if (seconds <= 0) {
        clearInterval(countdown);
        checkInternet();
      }
    }, 1000);

    function checkInternet() {
      fetch("https://www.google.com/favicon.ico", { mode: 'no-cors' })
        .then(() => {
          status.textContent = "✅ Internet Connected";
          setTimeout(() => window.location.href = "http://fi6.bot-hosting.net:21240/", 1000);
        })
        .catch(() => {
          status.textContent = "⚠️ Please Check Your Internet Connection";
          counter.style.display = "none";
        });
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
