function loadDoc() {
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "https://amhep.pythonanywhere.com/grades";
    const async = true;
    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function () {
        document.getElementById("0").innerHTML = this.responseText;
    };
}

function loadDoc1() {
    var first = document.getElementById("first").value;
    var last = document.getElementById("last").value;
    let fullname = first + " " + last;
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "https://amhep.pythonanywhere.com/grades/";
    const async = true;
    xhttp.open(method, url + fullname, async);
    xhttp.send();
    xhttp.onload = function () {
        document.getElementById("1").innerHTML = this.responseText;
    };
}



function loadDoc2() {
    var student1 = document.getElementById("nombre").value;
    var nota = document.getElementById("percent").value;
    var xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = { "name": student1, "grade": Number(nota) };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function () {
        let data = this.responseText;
        data = JSON.parse(data);
        Object.entries(data).forEach(([key, value]) => {
            if (key == student1) {
                document.getElementById("2").innerHTML = key + ": " + value;
            }
        });
    };
}

function loadDoc3() {
    var nickname = document.getElementById("nickname").value;
    var percentage = document.getElementById("percentage").value;
    const async = true;
    var xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades/";
    xhttp.open("PUT", url + nickname, async);
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = { "grade": Number(percentage) };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function () {
        let data = this.responseText;
        data = JSON.parse(data);
        Object.entries(data).forEach(([key, value]) => {
            if (key == nickname) {
                document.getElementById("3").innerHTML = key + ": " + value;
            }
        });
    };
}

function loadDoc4() {
    var count = 0;
    var person = document.getElementById("person").value;
    const xhttp = new XMLHttpRequest();
    var url = "https://amhep.pythonanywhere.com/grades/";
    const method = "DELETE";
    const async = true;
    xhttp.open(method, url + person, async);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send();
    xhttp.onload = function () {
        let data = this.responseText;
        data = JSON.parse(data);
        Object.entries(data).forEach(([key, value]) => {
            if (key == person) {
                count++;
            }
        });
        if(count == 0){
            document.getElementById("4").innerHTML = this.responseText;
        }
    };
}