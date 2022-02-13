# Simple-python-bot-for-10fastfingers


# steps

1. Clone the repo
   ```sh
   git clone https://github.com/ramesh1212445/Simple-python-bot-for-10fastfingers.git
   ```
2. install keyboard python package
```sh
pip install keyboard
```

3. save javascript code inside a bookmark

```sh
javascript: if (typeof console.save === "undefined") {
  console.save = function (data, filename) {
    if (!data) {
      console.error("Console.save: No data");
      return;
    }

    if (!filename) filename = "console.json";

    if (typeof data === "object") {
      data = JSON.stringify(data, undefined, 4);
    }

    var blob = new Blob([data], { type: "text/json" }),
      e = document.createEvent("MouseEvents"),
      a = document.createElement("a");

    a.download = filename;
    a.href = window.URL.createObjectURL(blob);
    a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
    e.initMouseEvent(
      "click",
      true,
      false,
      window,
      0,
      0,
      0,
      0,
      0,
      false,
      false,
      false,
      false,
      0,
      null
    );
    a.dispatchEvent(e);
  };
}

function fun1() {
  var list = [];
  for (let i = 0; i < document.querySelector(".place").childElementCount; i++) {
    let word = document.querySelector(".place").children[i].textContent;
    list.push(word);
  }
  console.save(list, "words.txt");
}

fun1();
```

4. visit [10ff.net] (https://10ff.net/)

5. open the saved bookmark

6. Save the word.txt in same folder 

5. execute 10ff.py
