/* =====================
Old search function that
called search.cfm 
=========================*/

var DocRemote = 0;

function makeRemote(){

	if(DocRemote){
		if(DocRemote.closed){
			DocRemote = 0;
			makeRemote();
		}else{
			DocRemote.focus();
		}
	}else{
		DocRemote = window.open('../button.htm', 
					    'Search', 
					    'scrollbars,resizable,width=510,height=300');
    	}
}


/*******************************
   winOpen()
   
        Open new window
        This script can be inserted into the existing SCRIPT
        block in the HEAD section, or placed anywhere in the
        document (with the SCRIPT tags) BEFORE the function is
        called by a link in the page.
        In addition to calling the script via 
        href="javascript:winOpen(***newpage***)",
        you can also call it using the 
        onclick="winOpen(***newpage***)" attribute;
        see the samples below.
   
   Author: Robert Crooks
   Date Created: 5/10/99
*******************************/
function winOpen(page) {
var newWindow = null;
// to adjust the location of the new window, change the left and top values (pixels)
// to adjust the size of the new window, change the width and height values (pixels)
newWindow = window.open(page,'externalWindow','width=445,height=235,scrollbars=Yes,location=No,left=200,top=100,menubar=No,resizable=Yes,toolbar=No');
newWindow.focus();   
}

function jumpOpen(page) {
var jumpWindow = null;
// to adjust the location of the new window, change the left and top values (pixels)
// to adjust the size of the new window, change the width and height values (pixels)
jumpWindow = window.open(page,'jumpWindow');
jumpWindow.focus();   
}



var folder = "";

function initFolder(){
	if (navigator.appName.indexOf('Microsoft') != -1 && navigator.appVersion.indexOf('Mac') != -1 && navigator.userAgent.indexOf('MSIE 4') == -1){
		folder = "";
	}
}
//launch search applet
function showSearch(){
	searchApplet.makeAppear();
}