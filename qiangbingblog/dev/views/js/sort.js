<script language="javascript">

function addSelected(fld1,value1,text1){
    if (document.all)    {
            var Opt = fld1.document.createElement("OPTION");
            Opt.text = text1;
            Opt.value = value1;
            fld1.options.add(Opt);
            Opt.selected = true;
    }else{
            var Opt = new Option(text1,value1,false,false);
            Opt.selected = true;
            fld1.options[fld1.options.length] = Opt;
    }
}
</script>