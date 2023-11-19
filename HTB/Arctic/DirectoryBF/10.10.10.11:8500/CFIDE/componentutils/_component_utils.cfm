








	
		
		
		

	




	






<html>
<head><script type="text/javascript" src="/CFIDE/scripts/cfform.js"></script>
<script type="text/javascript" src="/CFIDE/scripts/masks.js"></script>

	<title>Component Browser Login</title>
	
	
<style>
body, p, td {
	font-family: Arial, Helvetica, sans-serif;

	font-size: small;

}

th {
 font-family: Arial, Helvetica, sans-serif;
 font-size: small; ! important;
}

th {
 text-align:left;
}
.adminbody {
	background-color: #c4c4c4;
}

.resourcelist {
	list-style-type:square;
	margin-top:5px;
	margin-bottom:10px;
}

.errorText {
	color: #CC0000; 
}

.successText {
	color: #008800; 
}

.loginWhiteText {
	color: #FFFFFF; 
	font-weight: bold;
}

.loginInvalidText {
	color: #CC0000; 
	font-weight: bold;
}

.loginCopyrightText {
	color: #000000;
	font-size: 9px;
	font-family:Arial, Helvetica, sans-serif;
}

a {
	color: #003399;
	text-decoration: none;
}

a:hover {
	color: #008A00; 
}

.iconLinkText {
	color: #FFFFFF;
	font-weight: bold;

	font-size: small;

}

.leftMenuLinkText {
	color: #6C7A83; 

	font-size: small;

}

.leftMenuLinkTextHighlighted {
	color: #123f61; 

	font-size: small;

	font-weight:bold;
}

.topMenuLinkText {
	color: #000000;
	font-size: x-small; 
}

.menuCFAdminText {
	color: #000000;
	font-weight: bold;
	

	font-size: small;

}

.menuAuxText {
	color: #6C7A83;
	
		font-size: small;
	
}

.menuHeaderText {
	color: #0072AC;
	font-weight: bold;

	font-size: x-small;

	text-transform:uppercase;
}

.menuTD {
	/*border-top-width: 1px;
	border-right-width: 1px;
	border-bottom-width: 1px;
	border-left-width: 1px;
	border-top-style: none;
	border-right-style: none;
	border-bottom-style: solid;
	border-left-style: none;
	border-bottom-color: #CCCCCC;*/
	background: #ececec;
}

.menuTDHeader {
	/* can delete me thinks */
	/*border-top-width: 1px;
	border-right-width: 1px;
	border-bottom-width: 1px;
	border-left-width: 1px;
	border-top-style: solid;
	border-right-style: none;
	border-bottom-style: solid;
	border-left-style: none;*/
	background: #ececec url('../administrator/images/cap_menuitem_background.png') repeat-x;
}
.menuTDHeaderLeft {
	border-left-style:solid;
	border-left-width: 1px;
	border-color: #c4c4c4;
	background: #ececec url('../administrator/images/cap_menuitem_background.png') repeat-x;
}
.menuTDHeaderRight {
	border-right-style:solid;
	border-right-width: 1px;
	border-color: #c4c4c4;
	background: #ececec url('../administrator/images/cap_menuitem_background.png') repeat-x;
}

h1 {
	color: #000000;
	font-weight: bold;
	font-size: x-small;
	margin-top: 5px;
	margin-bottom: 5px;
}

.pageHeader {
	color: #0072AC;
	font-weight: bold;
	font-size: medium;
	margin-top: 5px;
	margin-bottom: 5px;
}

.currentuser {
	color: #0072AC;
	font-weight: bold;
	font-size: x-small;
	margin-top: 5px;
	margin-bottom: 5px;
}

.cellBlueSides {
	border-right-width: 1px;
	border-left-width: 1px;
	border-right-style: solid;
	border-left-style: solid;
	border-right-color: #C1D9DB;
	border-left-color: #C1D9DB;
}

.cellLeftBlueSide {
	border-left-width: 1px;
	border-left-style: solid;
	border-left-color: #D5E3E6;
}

.cellRightAndBottomBlueSide {
	border-right-width: 1px;
	border-right-style: solid;
	border-right-color: #D5E3E6;
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #D5E3E6;
}

.cell3BlueSides {
	border-left-width: 1px;
	border-left-style: solid;
	border-left-color: #D5E3E6;
	border-right-width: 1px;
	border-right-style: solid;
	border-right-color: #D5E3E6;
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #D5E3E6;
}

.cell4BlueSides {
	border-top-width: 1px;
	border-top-style: solid;
	border-top-color: #D5E3E6;
	border-left-width: 1px;
	border-left-style: solid;
	border-left-color: #D5E3E6;
	border-right-width: 1px;
	border-right-style: solid;
	border-right-color: #D5E3E6;
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #D5E3E6;
}

.cell2BlueSidesAndBlueBkgd {
	border-top-width: 1px;
	border-top-style: solid;
	border-top-color: #D5E3E6;
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #D5E3E6;
	background-color: #E8F0F1;
}

.cellBlueTop {
	border-top-width: 1px;
	border-top-style: solid;
	border-top-color: #C1D9DB;
}

.cellBlueBottom {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #C1D9DB;
}

.cellBlueTopAndBottom {
	border-top-width: 1px;
	border-top-style: solid;
	border-top-color: #C1D9DB;
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #C1D9DB;
}

.cellBordersBlue {
	border: 1px solid #C1D9DB;
}

.cellGrayBottom {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #E2E6E7;
}

.copyright {
	color: #000000;
	
		font-size: x-small;
	
}

.copyrightLink {
	color:#003399; 
	
		font-size: x-small;
	
}

.disabled {
	color: #999999;
}
.color-title		{background-color:888885;color:white;background-color:7A8FA4;}
.color-header		{background-color:ddddd5;}
.color-buttons		{background-color:ccccc5;}
.color-border		{background-color:666666;}
.color-row			{background-color:fffff5;}
.color-rowalert		{background-color:ffddaa;}
.buttn,.buttnText	{font-size:1em;font-family: tahoma,arial,Geneva,Helvetica,sans-serif;background-color:e0e0d5;}
</style>

	<meta name="Author" content="Copyright 1996-2023 Adobe Macromedia Software LLC. All rights reserved.">
<script type="text/javascript">
<!--
    _CF_checkloginform = function(_CF_this)
    {
        //reset on submit
        _CF_error_exists = false;
        _CF_error_messages = new Array();
        _CF_error_fields = new Object();
        _CF_FirstErrorField = null;


        //display error messages and return success
        if( _CF_error_exists )
        {
            if( _CF_error_messages.length > 0 )
            {
                // show alert() message
                _CF_onErrorAlert(_CF_error_messages);
                // set focus to first form error, if the field supports js focus().
                if( _CF_this[_CF_FirstErrorField].type == "text" )
                { _CF_this[_CF_FirstErrorField].focus(); }

            }
            return false;
        }else {
            return true;
        }
    }
//-->
</script>
</head>

<!-- frame buster - code by Gordon McComb -->
<script language="JavaScript" type="text/javascript">
	<!-- Hide script from older browsers

	function changePage() 
	{
		if(top != self) top.location = document.location;
	}

	function openWin( windowURL, windowName, windowFeatures ) { 
		return window.open( windowURL, windowName, windowFeatures ) ; 
	} 
	function open_on_entrance(url,name)
	{ 
	new_window = window.open(url, name, ' menubar,scrollBars,resizable,dependent,status,width=525,height=300')
	}
// -->
</script>

  

<body bgcolor="#6C7A83" onLoad="changePage();document.forms.loginform.j_password.focus();">




<form name="loginform" id="loginform" action="/CFIDE/componentutils/_component_utils.cfm?" method="POST" onsubmit="return _CF_checkloginform(this)">



<table>
	<tr>
		<td><img src="../administrator/images/spacer.gif" width="1" height="100"></td>
	</tr>
</table>
			
<table width="570" border="0" cellspacing="0" cellpadding="0" align="center" background="../administrator/images/componentutilslogin.jpg">
		<tr>
			<td colspan="4"><img src="../administrator/images/spacer.gif" width="1" height="115"></td>
		</tr>
		<tr>
			<td rowspan="5"><img src="../administrator/images/spacer.gif" width="25" height="1"></td>
			<td align="left">
				<table>
					<tr>
						<td nowrap="nowrap">				
				
					<p style="font-weight:bold;margin:0px 0px 0px 0px;">
Enter your RDS or Admin password below
</p>
					
				
				


				<p style="font-weight:bold;margin:5px 0px 5px 0px;">
Password
</p>
				<input name="j_password_required" type="hidden" value="Password Required">
				<input name="j_password" type="Password" size="15" maxlength="100" id="admin_login" autocomplete="off" style="width:300px; padding-left:5px;">
						</td>
					</tr>
				</table>
			</td>
			<td width="200px" class="loginInvalidText">
				<p style="margin:88px 0px 0px 0px;">
				
				</p>
			</td>
			<td rowspan="5"><img src="../administrator/images/spacer.gif" width="15" height="1"></td>
			</td>
		</tr>	
		<tr>
			<td align="left" colspan="2">
				


				<input name="submit" type="submit" value="Login" class="buttn-fix" style=" margin:7px 0px 0px 2px;;width:80px">
			</td>
		</tr>
		<tr>
	<td colspan="2">
		<table border="0" cellpadding="0" cellspacing="0">
			<tr>
				<td style="vertical-align:middle;"><img src="../administrator/images/spacer.gif" width="10" height="1"/><img src="../administrator/images/adobelogo.gif" width="29" height="32"/>
				<td style="width:500px;"><p style="margin:20px 20px 20px 20px;" class="loginCopyrightText">
Adobe, the Adobe logo, ColdFusion, and Adobe ColdFusion are trademarks or registered trademarks of Adobe Systems Incorporated in the United States and/or other countries.  All other trademarks are the property of their respective owners.
</p>
				</td>
			</tr>
		</table>
		<br />
	</td>
</tr>
</table>


</form>

</body></html>



	