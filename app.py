from flask import Flask, request
import openai
from googletrans import Translator

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"
translator = Translator()
# HTML code for the form
form_html = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Osana.IMG</title>
    <style>
      /* Add your CSS here to make the form responsive */

      * {
        box-sizing: border-box;
      }

      body {
        background: linear-gradient(to right, #9578ff, #e07aff);
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
        padding: 0;
      }
      h1{
        font-size: 100px;
        font-style: italic;
        background: linear-gradient(to left, #190072, #4d0064);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
        
      }
      /* Header/Blog Title */
      .header {
        padding: 1px;
        text-align: center;
      }

      /* Style the input field */
      input[type="text"] {
        width: 90%;
        padding: 15px;
        margin: 5px 0 22px 0;
        border: none;
        background: #f1f1f1;
        border-radius: 10px;
        font-size: 18px;
        line-height: 24px;
        color: #333;
        margin: 5px auto 22px auto;
        display: block;
        transition: transform 0.3s ease-in-out;
      }

      input[type="text"]:focus {
        border-color: #562266;
        border-style: solid;
        border-width: 5px;
        outline: none;
      }
      input[type="text"]:hover {
  transform: scale(1.02);
}

      .para1{
        font-size: 30px;
        bottom: 10px;
      }

      /* Style the submit button */
      .btn {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #590074;
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        width: 20%;
        opacity: 0.9;
        font-size: 18px;
        line-height: 24px;
        transition: opacity 0.2s ease-in-out;
        border-radius: 30px;
        margin: 0 auto;
        border: none;
                
}

      .btn:hover {
        opacity: 1;
        background-color: #2d004b;
      }

      /* Add a background color and some padding around the image */
      img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        padding: 20px;
      }

      /* Loader */
     .loader {
  width: 100%;
  height: 10px;
  background-color: #ddd;
  margin-bottom: 20px;
  display: none;
}

.bar {
  height: 100%;
  background-color: #3c0257;
  width: 0%;
  transition: width 1s ease-out;
}

@keyframes progress {
  0% {width: 0%}
  100% {width: 100%}
}


      .slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
  margin-top: 80px;
}

.mySlides {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
  z-index: -1;
}

.mySlides.fade {
  opacity: 1;
  z-index: 1;
}

.caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  font-size: 20px;
  padding: 10px;
  text-align: center;
}

.prev,
.next {
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 20px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

.prev {
left: 0;
}

.next {
right: 0;
}

.prev:hover,
.next:hover {
background-color: rgba(0, 0, 0, 0.8);
}

/* Add media query for small screens */
@media only screen and (max-width: 768px) {
  .slideshow-container {
    max-width: 100%;
    margin-top: 60px;
  }

  .mySlides {
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 1s ease-in-out;
    z-index: -1;
  }

  .mySlides.fade {
    opacity: 1;
    z-index: 1;
  }

  .caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    font-size: 16px;
    padding: 10px;
    text-align: center;
  }

  .prev,
  .next {
    position: absolute;
    top: 50%;
    width: auto;
    margin-top: -22px;
    padding: 16px;
    color: white;
    font-weight: bold;
    font-size: 16px;
    transition: 0.6s ease;
    border-radius: 0 3px 3px 0;
    user-select: none;
  }

  .prev {
    left: 0;
  }

  .next {
    right: 0;
  }

  .prev:hover,
  .next:hover {
    background-color: rgba(0, 0, 0, 0.8);
  }
}


      /* Extra small devices (phones) */
@media only screen and (max-width: 576px) {
  h1 {
    font-size: 50px;
  }
  input[type="text"] {
    width: 70%;
    font-size: 80%;
  }
  .btn {
    width: 50%;
  }
  img {
    width: 80%;
  }
  .para1{
        font-size: 20px;
     
      }
}

/* Small devices (tablets) */
@media only screen and (min-width: 576px) and (max-width: 768px) {
  h1 {
    font-size: 70px;
  }
  input[type="text"] {
    width: 70%;
  }
  .btn {
    width: 40%;
  }
  img {
    width: 60%;
  }
}

/* Medium devices (desktops) */
@media only screen and (min-width: 768px) and (max-width: 992px) {
  h1 {
    font-size: 80px;
  }
  input[type="text"] {
    width: 60%;
  }
  .btn {
    width: 30%;
  }
  img {
    width: 50%;
  }
}

/* Large devices (large desktops) */
@media only screen and (min-width: 992px) {
  h1 {
    font-size: 100px;
  }
  
  .btn {
    width: 20%;
  }
  img {
    width: 40%;
  }
}

    </style>
  </head>
  <body>
    <div class="header">
      <h1>Osana.IMG</h1>
      <p class="para1">We take great pains to make a picture of the thought that is in your mind.</p>
    </div>
    <form action="/" method="post">
      <input type="text" id="prompt" name="prompt" placeholder="Enter your imagination in here : " required>
      <button type="submit" class="btn">Generate Image</button>
      <br>
      <br>
      <div class="loader">
  <div class="bar"></div>
  </div>

  

      
    </form>

    <div class="slideshow-container">

      <div class="mySlides fade">
        <img src="https://external-preview.redd.it/Lql1jhwKxaH4oUAQX3U3Zau7iEv0TXEbJKyQMwM9mKI.jpg?auto=webp&s=0a0e1b37dffe79043c6ec640e15a5b6237a1d43d" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
    

      <div class="mySlides fade">
        <img src="https://i.kinja-img.com/gawker-media/image/upload/c_fit,f_auto,g_center,q_60,w_1315/726cf84bbeb42b33068c07b0f736fb41.jpg" alt=" Best images genarated by Osana.IMG">
        <div class="caption"> Best images genarated by Osana.IMG”</div>
      </div>
    
      <div class="mySlides fade">
        <img src="https://pbs.twimg.com/media/FRnjwCTXMAEJ5Ao.jpg:large" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
    
      <div class="mySlides fade">
        <img src="https://the-decoder.com/wp-content/uploads/2022/09/mona_lisa_dall_e_2-770x770.jpeg.webp" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
    
      <div class="mySlides fade">
        <img src="https://i.kinja-img.com/gawker-media/image/upload/q_75,w_1600,h_900,c_fill/0bf183cd60d66bddc13b48d84e6f353f.JPG" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
      
      <div class="mySlides fade">
        <img src="https://i.ytimg.com/vi/qY1nUu4h5Vc/maxresdefault.jpg" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
      
      <div class="mySlides fade">
        <img src="https://th.bing.com/th/id/R.8473d5a4a2bbcd3b15a46ca41ecf199c?rik=F8Oxznp3xk9JpQ&pid=ImgRaw&r=0" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
      
      <div class="mySlides fade">
        <img src="https://th.bing.com/th/id/R.eac7c1a84856ff86c772099fb86a7b26?rik=xKFQV0XctJl%2fuQ&riu=http%3a%2f%2fwww.rumormillnews.com%2fpix8%2fdeep_mind_art.jpg&ehk=fmFWSWInTYPXoZzLllm0wMKqP6FX%2bAkGDjGxmXFieSk%3d&risl=&pid=ImgRaw&r=0" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
      
      <div class="mySlides fade">
        <img src="https://lifeboat.com/blog.images/ai-generated-art-scene-explodes-as-hackers-create-groundbreaking-new-tools2.jpg" alt="Best images genarated by Osana.IMG">
        <div class="caption">Best images genarated by Osana.IMG</div>
      </div>
      



      <!-- Add more slides as needed -->
    
      <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
      <a class="next" onclick="plusSlides(1)">&#10095;</a>
    </div>
    

    <script>
      const loader = document.querySelector(".loader");
const bar = document.querySelector(".bar");
const form = document.querySelector("form");

function startLoading() {
  bar.style.width = "0%";
  loader.style.display = "block";
  setTimeout(() => {
    bar.style.width = "100%";
    setTimeout(() => {
      bar.style.width = "0%";
      setTimeout(() => {
        startLoading();
      }, 1100);
    }, 3000);
  }, 100);
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  startLoading();
});


      form.addEventListener('submit', (event) => {
        event.preventDefault();
        loader.style.display = 'block';
        setTimeout(() => {
          loader.style.display = 'none';
          form.submit();
        }, 2000);
      });


        var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].classList.remove("fade");
    slides[i].style.opacity = 0;
  }
  slides[slideIndex - 1].classList.add("fade");
  slides[slideIndex - 1].style.opacity = 1;
}

setInterval(function() {
  plusSlides(1);
}, 5000);

    </script>
</body>
</html>

'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #translator = Translator()
        prompt = request.form['prompt']
        print(prompt)
        #translated_prompt = translator.translate(prompt, dest="en")
        # Generate image using OpenAI's API
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        # Get URL of generated image
        image_url = response['data'][0]['url']

        # HTML code for the result page
        result_html = f'''
        <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Generated Image</title>
    <style>
        /* Add your CSS here to style the image */
        body {{
          background: linear-gradient(to right, #9578ff, #e07aff);
          font-family: Arial, Helvetica, sans-serif;
          margin: 0;
          padding: 0;
        }}

        img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            padding: 20px;
        }}

        .btn {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #590074;
            color: white;
            padding: 16px 20px;
            border: none;
            cursor: pointer;
            width: 20%;
            opacity: 0.9;
            font-size: 18px;
            line-height: 24px;
            transition: opacity 0.2s ease-in-out;
            border-radius: 30px;
            margin: 0 auto;
            border: none;
        }}

        .btn:hover {{
            opacity: 1;
            background-color: #2d004b;
        }}
        a {{
  text-decoration: none;
}}

        /* Media queries for responsiveness */
        @media screen and (max-width: 768px) {{
            img {{
                width: 80%;
            }}

            .btn {{
                width: 40%;
            }}
        }}

        @media screen and (max-width: 480px) {{
            img {{
                width: 100%;
            }}

            .btn {{
                width: 60%;
            }}
        }}
    </style>
</head>
<body>
    <img src="{image_url}" alt="Generated Image">
    <a class="btn" href="{image_url}" download>Download Image</a>
</body>
</html>

        '''

        return result_html
    else:
        return form_html

if __name__ == '__main__':
    app.run(debug=True)
