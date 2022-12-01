///////////////UNBIASED
    const URL2 = "https://teachablemachine.withgoogle.com/models/2h73m7TG4/";

    let model2, webcam2, labelContainer2, maxPredictions2;

    // Load the image model and setup the webcam
    async function init2() {
        const modelURL2 = URL2 + "model.json";
        const metadataURL2 = URL2 + "metadata.json";

        // load the model and metadata
        // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
        // or files from your local hard drive
        // Note: the pose library adds "tmImage" object to your window (window.tmImage)
        model2 = await tmImage.load(modelURL2, metadataURL2);
        maxPredictions2 = model2.getTotalClasses();

        // Convenience function to setup a webcam
        const flip2 = true; // whether to flip the webcam
        webcam2 = new tmImage.Webcam(200, 200, flip2); // width, height, flip
        await webcam2.setup(); // request access to the webcam
        await webcam2.play(); //not currently playing on the website
        window.requestAnimationFrame(loop2); //not currently looping
        // console.log(webcam2)
      
        // append elements to the DOM
        document.getElementById("webcam-container2").appendChild(webcam2.canvas);
        // document.getElementById("webcam-container2").appendChild(document.createElement("h2"));

        labelContainer2 = document.getElementById("label-container2");
        for (let i = 0; i < maxPredictions2; i++) { // and class labels
            labelContainer2.appendChild(document.createElement("div"));
        }

      
    }

    async function loop2() {
        webcam2.update(); // update the webcam frame
        await predict2();
        window.requestAnimationFrame(loop2);
    }

    // run the webcam image through the image model
    async function predict2() {
        // predict can take in an image, video or canvas html element
        const prediction2 = await model2.predict(webcam2.canvas);
        for (let i = 0; i < maxPredictions2; i++) {
            const classPrediction2 =
                prediction2[i].className + ": " + prediction2[i].probability.toFixed(2);
            labelContainer2.childNodes[i].innerHTML = classPrediction2;
        }
    }




///////////////BIASED

    // More API functions here:
    // https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

    // the link to your model provided by Teachable Machine export panel
    const URL = "https://teachablemachine.withgoogle.com/models/P4ZhwqSMA/";

    let model, webcam, labelContainer, maxPredictions;

    // Load the image model and setup the webcam
    async function init() {
        const modelURL = URL + "model.json";
        const metadataURL = URL + "metadata.json";

        // load the model and metadata
        // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
        // or files from your local hard drive
        // Note: the pose library adds "tmImage" object to your window (window.tmImage)
        model = await tmImage.load(modelURL, metadataURL);
        maxPredictions = model.getTotalClasses();

        // Convenience function to setup a webcam
        const flip = true; // whether to flip the webcam
        webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
        await webcam.setup(); // request access to the webcam
        await webcam.play();
        window.requestAnimationFrame(loop);
          // console.log(webcam)


        // append elements to the DOM
        document.getElementById("webcam-container").appendChild(webcam.canvas);
        labelContainer = document.getElementById("label-container");
        for (let i = 0; i < maxPredictions; i++) { // and class labels
            labelContainer.appendChild(document.createElement("div"));
        }
    }

    async function loop() {
        webcam.update(); // update the webcam frame
        await predict();
        window.requestAnimationFrame(loop);
    }

    // run the webcam image through the image model
    async function predict() {
        // predict can take in an image, video or canvas html element
        const prediction = await model.predict(webcam.canvas);
        for (let i = 0; i < maxPredictions; i++) {
            const classPrediction =
                prediction[i].className + ": " + prediction[i].probability.toFixed(2);
            labelContainer.childNodes[i].innerHTML = classPrediction;
        }
    }


//Below is code for the buttons in the Celebrity Test Cases section of the website. When the button is pressed, it displays the results for the corresponding celebrity with the algorithm listed. This does not involve an API call; rather, we pretested each celebrity picture against our two models and hard-coded their results into the web page.
    
serenaButton = document.getElementById("serena-btn")
serenaResultsB = document.getElementById("serena-resultsB")
serenaButton.onclick = function(){
  serenaResultsB.innerHTML = "<p>Male: 100%</p><p>Female: 0%</p>"
};

serenaButton1 = document.getElementById("serena-btn1")
serenaResultsLB = document.getElementById("serena-resultsLB")
serenaButton1.onclick = function(){
  serenaResultsLB.innerHTML = "<p>Male: 0%</p><p>Female: 100%</p>"
};


jiminButton = document.getElementById("jimin-btn")
jiminResultsB = document.getElementById("jimin-resultsB")
jiminButton.onclick = function(){
  jiminResultsB.innerHTML = "<p>Male: 1%</p><p>Female: 99%</p>"
};

jiminButton1 = document.getElementById("jimin-btn1")
jiminResultsLB = document.getElementById("jimin-resultsLB")
jiminButton1.onclick = function(){
  jiminResultsLB.innerHTML = "<p>Male: 100%</p><p>Female: 0%</p>"
};

brunoButton = document.getElementById("bruno-btn")
brunoResultsB = document.getElementById("bruno-resultsB")
brunoButton.onclick = function(){
  brunoResultsB.innerHTML = "<p>Male: 17%</p><p>Female: 83%</p>"
};


brunoButton1 = document.getElementById("bruno-btn1")
brunoResultsLB = document.getElementById("bruno-resultsLB")
brunoButton1.onclick = function(){
  brunoResultsLB.innerHTML = "<p>Male: 100%</p><p>Female: 0%</p>"
};

kateButton = document.getElementById("kate-btn")
kateResultsB = document.getElementById("kate-resultsB")
kateButton.onclick = function(){
  kateResultsB.innerHTML = "<p>Male: 0%</p><p>Female: 100%</p>"
};

kateButton1 = document.getElementById("kate-btn1")
kateResultsLB = document.getElementById("kate-resultsLB")
kateButton1.onclick = function(){
  kateResultsLB.innerHTML = "<p>Male: 0%</p><p>Female: 100%</p>"
};