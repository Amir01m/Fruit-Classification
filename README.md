
<h1>🍎 Fruit Classification</h1>

<p>
This project is a simple fruit image classifier made with Python and Tkinter. 
It can identify <b>apples</b> and <b>bananas</b> from images. 
The user can choose an image, and the program predicts which fruit is in the image.
</p>

<hr>

<h2>📌 How the Program Works</h2>

<h3>1️⃣ Dataset Preparation</h3>
<p>
The dataset is stored in the <code>dataset/</code> folder. Images are:
</p>
<ul>
    <li>Resized to <b>280x280 pixels</b></li>
    <li>Flattened into a 1D array for the classifier</li>
</ul>

<h3>2️⃣ Feature and Label Extraction</h3>
<p>
The program separates features and labels:
</p>
<ul>
    <li><code>x</code> contains the image data</li>
    <li><code>y</code> contains the labels ("apple" or "banana")</li>
</ul>

<hr>

<h3>3️⃣ Training the Classifier</h3>
<p>
The project uses <code>KNeighborsClassifier</code> from <code>scikit-learn</code>. Steps:
</p>
<ul>
    <li>Split dataset into training and test sets (<code>train_test_split</code>)</li>
    <li>Train the KNN model with <code>xtrain</code> and <code>ytrain</code></li>
    <li>Predict fruits for the test or user-provided images</li>
</ul>

<hr>

<h3>4️⃣ User Interface (GUI)</h3>
<p>
The program uses Tkinter GUI, which includes:
</p>
<ul>
    <li>A <b>Choose File</b> button to select an image</li>
    <li>A label showing the predicted fruit</li>
    <li>A canvas for possible future visualization</li>
    <li>An <b>Exit</b> button to close the program</li>
</ul>

<hr>

<h3>5️⃣ How to Use</h3>
<ol>
    <li>Run <code>main.py</code> with Python 3.x</li>
    <li>Click "Choose File" and select an image of apple or banana</li>
    <li>The program will display the predicted fruit in the label</li>
    <li>Click "Exit" to close the application</li>
</ol>

<hr>

<h2>📁 Requirements</h2>
<p>
Required Python libraries:
</p>
<ul>
    <li><code>numpy</code></li>
    <li><code>Pillow (PIL)</code></li>
    <li><code>scikit-learn</code></li>
    <li><code>tkinter</code> (included in standard Python)</li>
</ul>

<p>
Install missing packages with pip:
</p>
<pre>
pip install numpy pillow scikit-learn
</pre>

<hr>

<h2>▶ Running the Program</h2>
<pre>
python main.py
</pre>

<hr>

<h2>✔ Project Structure</h2>
<pre>
Fruit-Classification/
│
├── main.py
├── dataset/
│   ├── apple/
│   └── banana/
└── README.html
</pre>

<hr>

<h2>💡 Notes</h2>
<ul>
    <li>Currently, only apples and bananas are supported.</li>
    <li>The model uses a small dataset, so predictions may not be accurate for unseen images.</li>
    <li>Images are resized and flattened for KNN input.</li>
</ul>

</body>
</html>
