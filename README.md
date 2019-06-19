Django Media Placeholder
=========================

This project override django `static media` and `storage`(optional), for process every media request, if media not present locally, and try to obtain in another location

Its great for dev, homolog and QA ambients because no need to copy production media every time.

Installation
------------

1. Install the package with:

    `pip install django-media-placeholder`

2. Uninstall the package with:

    `pip uninstall django-media-placeholder`

3. Add and URL to your URLCONF:
    ```
    from django_media_placeholder.static import static
    urlpatterns = [
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

4. On `settings.py`, set `MEDIA_URL` to point to it
    ```
    ...
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
    STATIC_ROOT = os.path.join(DATA_DIR, 'static')
    ALTERNATIVE_MEDIA_URL = 'Url to Get image not present in locally'
    ```

5. If use thumbanails, set `DEFAULT_FILE_STORAGE` to new storage,
(thumbnails's libs generate and get image directly in disk, no request to media path):
    ```
    DEFAULT_FILE_STORAGE = 'django_media_placeholder.custom_storage.OverwritingStorage'
    ```
