quoteDict = {
    1: "*breaks wall* OH YEAHHHHH",
    2: "A boat's a boat but the mystery box could be anything it could even be a boat",
    3: "Who the fuck starts a conversation like that?! I just sat down!",
    4: "Roadhouse",
    5: "Death to America <br> And butter sauce <br> Don't boil me <br> I'm still alive <br> Iraq Lobster <br> Iraq Lobster" 
}

def GetQuote(randomNumber):
    quote = quoteDict.get(randomNumber)
    return quote


def ReturnHTML(quoteString):
    htmlString = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Random Family Guy Quote</title>
<style>
body {{
    margin: 0;
    font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #e6eef8;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    text-align: center;
    padding-top: 100px;

    background-image: url("https://media.tenor.com/eFdq5SC5XnkAAAAM/family-guy-peter-griffin.gif");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}}

h1, h2, h3, h4, h5 {{
    letter-spacing: -0.5px;
    color: black;
    text-shadow: 2px 2px #ffffff;
    margin: 0; 
}}

h1 {{
    font-size: 4rem;
    margin-bottom: 0.3rem;
}}

img {{
    max-width: 280px;
    width: 100%;
    height: auto;
    display: block;
    margin: 0.3rem 0;
    filter: drop-shadow(2px 2px 8px rgba(0, 0, 0, 0.7));
}}

h2 {{
    font-size: 4rem;
    margin-top: 0.3rem;
}}

h3 {{
    font-size: 2.5rem;
    font-style: italic;
    margin-top: 2rem;
}}

h4 {{
    font-size: 1.2rem;
    max-width: 800px;
    line-height: 1.5;
    margin-top: 1rem;
}}

h5 {{
    margin-top: 0.3rem;
    font-size: 10rem;
}}
</style>
</head>
<body>
<h1>Random</h1>
<img
src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Family_Guy_Logo.svg/1200px-Family_Guy_Logo.svg.png"
alt="Family Guy logo"
/>
<h2>Quote</h2>

<h3>"{quoteString}"</h3>

<h4>"Brian, don't you know that randomfamilyguyquote.com is the word? Well everyone knows that randomfamilyguyquote.com is the word!"</h4>

<h5>Mom says I'm special</h5>

</body>
</html>
"""
    return htmlString
