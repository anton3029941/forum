## ENDPOINTS
    '/' — homepage
    '/create' — writing a post

    '/post/<int:post_id>' — viewing a post
    '/post/<int:post_id>/replies' — viewing replies to a post
    '/post/<int:post_id>/reply' — publish a reply to a post
    '/post/<int:post_id>/reply/delete' — delete a reply (author of the post)

    '/post/<int:post_id>/delete' — delete a post (author only)
    '/post/<int:post_id>/edit' — edit a post (author only)

    '/login' — log in an account
    '/log_out' — log out from an account
    '/register' — create an account