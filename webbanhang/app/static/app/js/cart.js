let updateBtns;
updateBtns = document.getElementsByClassName('update-cart');
for (let i=0;i < updateBtns.length; i++)
    {
        updateBtns[i].addEventListener('click', function ()
        {
            let productId = this.dataset.product
            let action = this.dataset.action
            console.log('productID', productId, 'action', action)
            console.log('user', user)
            if (user === "AnonymousUser")
            {
                console.log('User does not login')
            }
            else
            {
                update_user_order(productId, action)
            }
        })
    }
function update_user_order(productId, action) {
    console.log('user login, success add')
    let url = '/home/update_item/'
    fetch(url,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({"productId":productId, "action": action}),
        })
        .then(response =>{
        return response.json()}
        )
        .then(data =>{
            console.log('data', data)
            location.reload()
        })
}
