<!DOCTYPE html>
<!--[if lt IE 7 ]> <html lang="en" class="no-js ie6"> <![endif]-->
<!--[if IE 7 ]>    <html lang="en" class="no-js ie7"> <![endif]-->
<!--[if IE 8 ]>    <html lang="en" class="no-js ie8"> <![endif]-->
<!--[if IE 9 ]>    <html lang="en" class="no-js ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--> <html lang="en" class="no-js"><!--<![endif]-->
	<head>
		<meta charset="utf-8">
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title><g:layoutTitle default="Grails"/></title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="shortcut icon" href="${resource(dir: 'images', file: 'favicon.ico')}" type="image/x-icon">
		<link rel="stylesheet" href="${resource(dir: 'font-awesome/css/', file: 'font-awesome.min.css')}" type="text/css">
		
		<g:layoutHead/>
		<g:javascript library="application"/>
				
		<r:require modules="bootstrap"/>
		
		<r:layoutResources />
		<g:javascript src="plugins/metisMenu/jquery.metisMenu.js" />
		<g:javascript src="sb-admin.js" />
		<g:javascript src="ajax.js" />

		<link href="font-awesome/css/font-awesome.css" rel="stylesheet">
 		<link href="css/sb-admin.css" rel="stylesheet">
		<link href="css/plugins/morris/morris-0.4.3.min.css" rel="stylesheet">
    	<link href="css/plugins/timeline/timeline.css" rel="stylesheet">
   		
	</head>
	<body>
		<g:layoutBody/>
		<r:layoutResources />
	</body>
</html>
