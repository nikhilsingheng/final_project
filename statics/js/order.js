var addItemId=0;
function addTocart(item){
    addItemId+=1;
    var selectedItem = document.createElement('div')
    selectedItem.classList.add('cartImg')
    selectedItem.setAttribute('id',addItemId)
    
    var img=document.createElement('img')
    img.setAttribute('src',item.children[0].currentSrc)
   
    var title=document.createElement('div');
    title.innerText=item.children[1].innerText;
    
    var price=document.createElement('div');
    price.innerText=item.children[2].innerText;

    var delBtn=document.createElement('button');
    delBtn.innerText='Delete'
    delBtn.setAttribute('onclick','del('+addItemId+')');
     
    
    var cartItems=document.getElementById('title')
    selectedItem.append(img)
    selectedItem.append(title)
    selectedItem.append(price)
    selectedItem.append(delBtn)

    cartItems.append(selectedItem);


}
function del (item){
    document.getElementById(item).remove();
}