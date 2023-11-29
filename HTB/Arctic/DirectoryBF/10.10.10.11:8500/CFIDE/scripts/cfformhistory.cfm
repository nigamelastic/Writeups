

<html>
<head>
<script type='text/javascript' language='JavaScript1.2' charset='utf-8'>
// Bug Number 66391. Added try catch block while getting the property Windows.vars to catch the permission denied exception.
try 
{
var v = new top.Vars(top.getSearch(window));
var fv = v.toString('$_');
} 
catch(e){}
</script>
</head>
<body >
<script type='text/javascript' language='JavaScript1.2' charset='utf-8'>

document.writeln('<object id="utility" name="cfformhistory.swf" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,14,0" width="100" height="50">');

document.writeln('<param name="movie" value="cfformhistory.swf" />');
// Bug Number 66391. Added try catch block while getting the property Windows.lc_id to catch the permission denied exception.
try
{
    document.writeln('<param name="FlashVars" value="'+fv+'&$_lconid='+top.lc_id+'"/>');
} 
catch(e) {}
document.writeln('<param name="quality" value="high" />');
document.writeln('<param name="bgcolor" value="#FFFFFF" />');
document.writeln('<param name="profile" value="false" />');
// Bug Number 66391. Added try catch block while getting the property Windows.lc_id to catch the permission denied exception.
try 
{
 document.writeln('<embed id="utilityEmbed" name="cfformhistory.swf" src="cfformhistory.swf" type="application/x-shockwave-flash" flashvars="'+fv+'&$_lconid='+top.lc_id+'" profile="false" quality="high" bgcolor="#FFFFFF" width="100" height="50" align="" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>');
} 
catch(e){}
document.writeln('</object>');
</script>
</body>
</html>
