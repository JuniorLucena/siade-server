/**
 * checkButton - Tranforma um checkbox em botao
 * Requer jquery
 */

function checkButton(selector, addClass, checkedClass) {
    checkedClass = checkedClass || "active"
    var ele = $(selector)
    ele.each(function(idx, val){
        $(val).addClass(addClass)
        var checkbox = $(val).find("input[type=checkbox]")
        checkbox.toggle()
        if(checkbox.attr("checked")) {
            $(val).toggleClass(checkedClass)
        }
    })
    ele.click(function(){
        var checkbox = $(this).find("input[type=checkbox]")
        checkbox.attr("checked", !checkbox.attr("checked"))
        $(this).toggleClass(checkedClass)
        return false
    })
}