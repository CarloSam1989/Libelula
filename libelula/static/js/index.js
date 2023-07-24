/*const listarproducto=async() => {
    try{
        const response = await fetch('http://127.0.0.1:8000/productos/');
        const data = await response.json();

        let content='';
        data.productos.array.forEach((producto, index) => {
            content += "
                <tr>
                    <td>${index}</td>
                    <td>${productos.nombre}</td>
                </tr>    
            ";
        });
    } catch (ex){
        alert(ex)
    }
}
window.addEventListener('load',async()=>{
    await listarproducto();
});*/