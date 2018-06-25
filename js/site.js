function switchem () {
    if (this.mostclr == 'green') {
	this.mostclr = 'lightblue';
    }
    else {
	this.mostclr = 'green';
    }
    document.getElementById('mostppl').style.background = this.mostclr;
	
}

