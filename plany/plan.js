function drukuj(){
	if(self.parent.frames.length<2)
		alert('Polecenie niedost�pne')
	else{
		self.parent.plan.focus()
		window.print()
	}
}