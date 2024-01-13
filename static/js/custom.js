function sendComment(articleId) {
    var comment = $('#comment').val();
    var parentId = $('#parent_id').val();
    $.get('/articles/send-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        $('#comments-region').html(res);
        $('#comment').val('');
        $('#parent_id').val('');
        if (parentId !== null && parentId !== '') {
            document.getElementById('comment-pointer').scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comments-region').scrollIntoView({behavior: "smooth"});
        }
    });
}

function replyComment(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_answer').scrollIntoView({behavior: "smooth"});
}

function showLargeImage(image) {
    $('#main_image').attr('src', image);
    $('#btn-product-gallery').attr('href', image)
}

function addProduct(productId) {
    const count = $('#quantity').val();
    $.get('/order/add-product-order?product_id=' + productId + '&count=' + count).then(res => {
        if (res.status === 'success') {
            Swal.fire({
                title: 'عملیات موفق',
                text: "محصول مورد نظر به سبد خرید شما اضافه شد.",
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'تسویه حساب'
            }).then((result) => {

            })
        } else if (res.status === 'not_login') {
            Swal.fire({
                title: 'عملیات ناموفق',
                text: "برای خرید محصول باید وارد سایت شوید.",
                icon: 'warning',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'ورود به سایت'
            }).then((result) => {
                if (result.isConfirmed && res.status === 'not_login') {
                    window.location.href = '/register/'
                }

            })
        } else if (res.status === 'product_not_found') {
            Swal.fire({
                title: 'عملیات ناموفق',
                text: "محصول مورد نظر یافت نشد",
                icon: 'error',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'رفتن به فروشگاه'
            }).then((result) => {

            })
        }
    })
}

function deleteFromOrderItems(itemId) {
    $.get('/my-account/delete-order-item?detail_id=' + itemId).then(res => {
        if (res.status === 'success') {
            $('#item-content').html(res.data);
        }
    })
}

function changeItemCount(itemId, position) {
    $.get('/my-account/change-item-count?item_id' + itemId + '&position=' + position).then(res => {
        if (res.status === 'success') {
            $('#item-content').html(res);
        }
    });
}