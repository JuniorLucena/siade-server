<%@ page import="com.br.holocronifrn.siadeserver.User" %>

<table class="table table-striped table-bordered table-hover dataTable no-footer">
    <thead>
        <tr>
            <th>Barra</th>
            <th>Nome</th>
            <th>Campanha</th>
            <th>Setor</th>  
            <th>Editar</th> 
            <th>Adicionar</th>                                          
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
                    <input class="form-control" id="user_${it.id}" placeholder="Enter text" type="text" data-provide="typeahead" onfocus="searchDistricts('user_${it.id}')">
                </td>

                <td>
                    <i class="fa fa-gear fa-fw"></i>
                </td>

                <td>
                    <i class="fa fa-plus"></i>
                </td>
            </tr>                                 
        </g:each>
       
    </tbody>
</table>          
    
<script>
    $(function() {
        $.ajax({
            type: "GET",
            url: "<g:createLink controller='district' action='getDistricts' />",
            dataType: "json",            
            success: function(data, textStatus) {
                var districts = []
                $.each( data, function( key, value ) {
                    districts.push(value.name)
                });
                $("input[id^='user_']").typeahead({
                    source: districts
                })
            }
        });
    });
</script>

