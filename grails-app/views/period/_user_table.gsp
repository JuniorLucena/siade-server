<%@ page import="com.br.holocronifrn.siadeserver.User" %>
<div id="wrapper">
        <div id="page-wrapper">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="page-header">Tables</h1>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Agentes de Endemias
                        </div>
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover" id="dataTables-example">
                                    <thead>
                                        <tr>
                                            <th>Barra</th>
                                            <th>Nome</th>
                                            <th>Campanha</th>
                                            <th>Setor</th>                                            
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <g:each in="${com.br.holocronifrn.siadeserver.User.list()}">
                                            <tr class="odd gradeX">
                                                <td>${it.code}
                                                <td>${it.name}</td>                                    
                                                <td>
                                                    <select class="form-control">
                                                        <option>Dengue</option>
                                                        <option>Chagas</option>
                                                        <option>Calazar</option>
                                                        <option>Raiva</option>
                                                    </select>
                                                </td>

                                                <td>                                    
                                                    <input class="form-control" id="districts_autocomplete" placeholder="Enter text" type="text" data-provide="typeahead">
                                                </td>
                                            </tr>                                 
                                        </g:each>
                                       
                                    </tbody>
                                </table>
                            </div>
   	                        <!-- /.table-responsive -->                      
                        </div>
                        <!-- /.panel-body -->
                    </div>
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->   
        </div>
        <!-- /#page-wrapper -->
    </div>
    <!-- /#wrapper -->

    <!-- Core Scripts - Include with every page -->
    
    
    <g:javascript src="plugins/metisMenu/jquery.metisMenu.js" />

    <!-- Page-Level Plugin Scripts - Tables -->
    <g:javascript src="plugins/dataTables/jquery.dataTables.js" />
    <g:javascript src="plugins/dataTables/dataTables.bootstrap.js" />

    <!-- SB Admin Scripts - Include with every page -->
    <g:javascript src="sb-admin.js" />

    <!-- Page-Level Demo Scripts - Tables - Use for reference -->
    <script>
    $(document).ready(function() {
        $('#dataTables-example').dataTable();
    });
    </script>

    <script>
        $(function() {
            $.ajax({
                type: "GET",
                url: "<g:createLink controller='district' action='getDistricts' />",
                dataType: "json",            
                success: function(data, textStatus) {
                    console.log(data)
                    var districts = []
                    $.each( data, function( key, value ) {
                        districts.push(value.name)
                    });

                    $('#districts_autocomplete').typeahead({
                        source: districts
                    })
                }
            });
        });
    </script>

