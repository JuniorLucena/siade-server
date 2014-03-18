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
		<title><g:layoutTitle default="Siade"/></title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		
		<g:layoutHead/>
		<g:javascript library="application"/>
				
		<r:require modules="bootstrap"/>
		
		<r:layoutResources />
		
		<g:javascript src="plugins/metisMenu/jquery.metisMenu.js" />
		<g:javascript src="sb-admin.js" />
		<g:javascript src="ajax.js" />
		<g:javascript src="jquery-ui-1.10.4.custom.min.js" />
		<g:javascript src="bootstrap-datepicker.js"/>
		<g:javascript src="bootstrap/bootstrap-typeahead.js" />

		<link rel="shortcut icon" href="${resource(dir: 'images', file: 'favicon.ico')}" type="image/x-icon">
		<link href="${resource(dir: 'css/font-awesome/css/', file: 'font-awesome.min.css')}" rel="stylesheet" type="text/css">
		<link href="${resource(dir: 'css/font-awesome/css', file: 'font-awesome.css')}" rel="stylesheet" type="text/css">
 		<link href="${resource(dir: 'css', file:'sb-admin.css')}" rel="stylesheet" type="text/css">		
		<link href="${resource(dir: 'css/plugins/morris', file: 'morris-0.4.3.min.css')}" rel="stylesheet" type="text/css">    	
    	<link href="${resource(dir: 'css/plugins/timeline', file: 'timeline.css')}" rel="stylesheet" type="text/css">
   		
	</head>
	<body>
		<g:layoutBody/>
		<r:layoutResources />
	</body>
</html>
