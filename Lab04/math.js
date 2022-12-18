class numerical {
    constructor(num, symbol, something, string, string2, highlight, prev, standard) {
        this.num = num;
        this.symbol = symbol;
        this.something = something;
        this.string = string;
        this.string2 = string2;
        this.highlight = highlight;
        this.prev = prev;
        this.standard = standard;
    }
}

var string1 = new numerical("", "", 0, "", "", "", "", "");
var solu = 0;
var temp = 0;
var limit = 0;

function myFunction(num) {
    if(string1.highlight != ""){
        ResetColor();
    }
    if (isNaN(typeof (num)) == true) {
        if ((num == ".") && (string1.num == "")) {
            string1.num = "0";
        }
        if ((limit != "1") || (num != ".")) {
            string1.num = string1.num + num;
            if (num == ".") {
                limit = "1";
            }
        }
    }
    document.getElementById("demo").innerHTML = string1.num;
}

function symbol(num) { 
    if (num == "÷" || num == "*" || num == "+" || num =="-") {
        string1.highlight = num;
        document.getElementById(num).style.backgroundColor='Yellow';
        string1.something = string1.something + 1;
        string1.symbol = num;
        if(string1.prev == ""){
            string1.prev = string1.symbol;
        }
        if (string1.num == "") {
            string1.num = "0";
        }
        if (string1.string == "") {
            string1.string = string1.num;
        }
        else if(string1.string2 == ""){
            string1.string2 = string1.num;
        }
        if((string1.string2 != string1.num) && (string1.string2 != "")){
            string1.string2 = string1.num;
        }
        temp = string1.symbol;
        string1.symbol = string1.prev; 
        string1.prev = temp;
        if((string1.string != "") && (string1.string2 != "") && (string1.something >= 2)){  
            string1.standard = string1.symbol;
            solve(string1.something);
            string1.string2 = string1.num;
        }
        string1.num = "";
        limit = 0;
        string1.standard = num;
        console.log(string1.prev)
    }
}

function ResetEntry() {
    string1.num = "";
    string1.string = "";
    string1.string2 = "";
    string1.something = 0;
    string1.prev = "";
    string1.symbol = "";
    string1.standard = "";
    ResetColor();
    document.getElementById("demo").innerHTML = 0;
}

function solve(num) {
    if(num == 0){
        ResetColor();
    }
    string1.something = num;
    if(string1.num != ""){    
        string1.string2 = string1.num;
    }
    if (string1.standard == "÷") {
        solu = (parseFloat(string1.string)) / (parseFloat(string1.string2))
    }
    if (string1.standard == "-") {
        solu = (parseFloat(string1.string)) - (parseFloat(string1.string2))
    }
    if (string1.standard == "+") {
        solu = (parseFloat(string1.string)) + (parseFloat(string1.string2))
    }
    if (string1.standard == "*") {
        solu = (parseFloat(string1.string)) * (parseFloat(string1.string2))
    }
    document.getElementById("demo").innerHTML = solu;
    string1.string = solu;
}

function ResetColor(){
    if(string1.highlight != ""){
        document.getElementById(string1.highlight).style.backgroundColor='Red';
    }
}