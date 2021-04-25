let darkMode = localStorage.getItem("darkMode")
const darkModeToggle = document.querySelector('#dark');


//check if dark mode is enabled
//if it's enabled, turn it off and vise-versa
//check if dark mode is enabled
//if it's enabled, turn it off and vise-versa


const enableDarkMode=()=>{
	//add the class
	document.body.classList.add('dark-mode');
	//update localstorage
	localStorage.setItem('darkMode', 'enabled');
};
const disableDarkMode=()=>{
	//remove the class
	document.body.classList.remove('dark-mode');
	//update localstorage
	localStorage.setItem('darkMode',null );
};

if(darkMode==="enabled"){
	enableDarkMode();
}



darkModeToggle.addEventListener("click",()=>{
	darkMode= localStorage.getItem("darkMode");
	if (darkMode!=='enabled'){
		enableDarkMode()
	}else{
		disableDarkMode();
	}

})

