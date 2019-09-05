# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class F2CAccessService(models.Model):
    mid = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    access_service_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    user_remarks = models.TextField(blank=True, null=True)
    admin_remarks = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    service_lang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_access_service'


class F2CAd(models.Model):
    aid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    pid = models.IntegerField()
    url = models.CharField(max_length=255)
    url_en = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    hits = models.IntegerField()
    addtime = models.DateTimeField(blank=True, null=True)
    edittime = models.DateTimeField(blank=True, null=True)
    fromtime = models.DateTimeField(blank=True, null=True)
    totime = models.DateTimeField(blank=True, null=True)
    image_src = models.CharField(max_length=255)
    image_src_en = models.CharField(max_length=255, blank=True, null=True)
    image_alt = models.CharField(max_length=100)
    image_alt_en = models.CharField(max_length=100, blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    keyword_en = models.CharField(max_length=100, blank=True, null=True)
    listorder = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField()
    author = models.CharField(max_length=30, blank=True, null=True)
    release_time = models.DateTimeField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_ad'


class F2CAdCategory(models.Model):
    acid = models.AutoField(primary_key=True)
    aid = models.IntegerField(blank=True, null=True)
    cateid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_ad_category'


class F2CAdPlace(models.Model):
    pid = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    price = models.FloatField()
    listorder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_ad_place'


class F2CArea(models.Model):
    areaid = models.AutoField(primary_key=True)
    areaname = models.CharField(max_length=50)
    areaname2 = models.CharField(max_length=200)
    parentid = models.IntegerField()
    arrparentid = models.CharField(max_length=255)
    child = models.IntegerField()
    arrchildid = models.TextField()
    listorder = models.SmallIntegerField()
    listorder2 = models.SmallIntegerField()
    flag = models.CharField(max_length=255, blank=True, null=True)
    national_pavilions = models.IntegerField(blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_area'


class F2CArticle(models.Model):
    aid = models.AutoField(primary_key=True)
    related = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hits = models.IntegerField(blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    edittime = models.DateTimeField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    image_src = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)
    catid = models.CharField(max_length=30)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    listorder = models.SmallIntegerField()
    status = models.IntegerField()
    author = models.CharField(max_length=30, blank=True, null=True)
    release_time = models.DateTimeField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_article'


class F2CArticleCat(models.Model):
    catid = models.AutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    cat_name = models.CharField(max_length=255, blank=True, null=True)
    cat_name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_article_cat'


class F2CAssociator(models.Model):
    user_id = models.IntegerField()
    company = models.CharField(max_length=255, blank=True, null=True)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=15, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    links = models.CharField(max_length=255, blank=True, null=True)
    main_product = models.TextField(blank=True, null=True)
    main_brand = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    business_licence = models.CharField(max_length=255, blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    out_time = models.DateTimeField(blank=True, null=True)
    is_recommend = models.IntegerField(blank=True, null=True)
    recommend_sort = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    more_catid = models.CharField(max_length=1000, blank=True, null=True)
    recommend_edit_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_associator'


class F2CAssociatorContacts(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    role_id = models.IntegerField()
    associator = models.ForeignKey(F2CAssociator, models.DO_NOTHING, unique=True)
    grade = models.IntegerField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    last_login_time = models.IntegerField(blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_associator_contacts'


class F2CAssociatorGrade(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    grade = models.CharField(max_length=32, blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_associator_grade'


class F2CAssociatorService(models.Model):
    service = models.CharField(max_length=30, blank=True, null=True)
    service_en = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_associator_service'


class F2CAuthorityMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=64)
    menu_name_en = models.CharField(max_length=64, blank=True, null=True)
    menu_uri = models.CharField(max_length=160, blank=True, null=True)
    parent_id = models.CharField(max_length=48, blank=True, null=True)
    menu_level = models.IntegerField()
    operation_security = models.IntegerField()
    menu_seq = models.IntegerField()
    menu_ico = models.CharField(max_length=48, blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    is_show = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'f2c_authority_menu'


class F2CAuthorityMenuOperation(models.Model):
    operation_id = models.BigAutoField(primary_key=True)
    menu_id = models.IntegerField()
    operation_name = models.CharField(max_length=48)
    operation_uri = models.CharField(max_length=160, blank=True, null=True)
    operation_ico = models.CharField(max_length=48, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_authority_menu_operation'


class F2CAuthorityRoleMenu(models.Model):
    role_id = models.IntegerField()
    menu_id = models.IntegerField()
    menu_uri = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_authority_role_menu'


class F2CBatchImageList(models.Model):
    bid = models.BigAutoField(primary_key=True)
    aid = models.IntegerField()
    old_file_name = models.CharField(max_length=255, blank=True, null=True)
    oss_file_neme = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_batch_image_list'


class F2CCategory(models.Model):
    catid = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=50)
    catname2 = models.CharField(max_length=255)
    linkurl = models.CharField(max_length=255)
    letter = models.CharField(max_length=4)
    level = models.IntegerField()
    property = models.SmallIntegerField()
    parentid = models.IntegerField()
    arrparentid = models.CharField(max_length=255)
    child = models.IntegerField()
    arrchildid = models.TextField()
    listorder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_category'


class F2CCategoryOld(models.Model):
    catid = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=50)
    catname2 = models.CharField(max_length=255)
    linkurl = models.CharField(max_length=255)
    letter = models.CharField(max_length=4)
    level = models.IntegerField()
    property = models.SmallIntegerField()
    parentid = models.IntegerField()
    arrparentid = models.CharField(max_length=255)
    child = models.IntegerField()
    arrchildid = models.TextField()
    listorder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_category_old'


class F2CChannelsInfo(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    channelid = models.IntegerField(db_column='channelId', blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(max_length=16, blank=True, null=True)
    livestatus = models.IntegerField(db_column='liveStatus', blank=True, null=True)  # Field name made lowercase.
    livetime = models.DateTimeField(blank=True, null=True)
    is_use = models.IntegerField(db_column='is_Use', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f2c_channels_info'


class F2CChinaTab(models.Model):
    mid = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    user_remarks = models.TextField(blank=True, null=True)
    admin_remarks = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    report = models.CharField(max_length=255, blank=True, null=True)
    document_introduction = models.CharField(max_length=1000, blank=True, null=True)
    tag_images = models.CharField(max_length=1000, blank=True, null=True)
    packing_images = models.CharField(max_length=1000, blank=True, null=True)
    certificate_images = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_china_tab'


class F2CCollection(models.Model):
    c_id = models.AutoField(primary_key=True)
    ac_id = models.IntegerField()
    type = models.IntegerField()
    type_id = models.IntegerField()
    status = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_collection'


class F2CCurrency(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    sign = models.CharField(max_length=1, blank=True, null=True)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_currency'


class F2CCustomsClearanceLogistics(models.Model):
    mid = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    user_remarks = models.TextField(blank=True, null=True)
    admin_remarks = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_customs_clearance_logistics'


class F2CDues(models.Model):
    did = models.AutoField(primary_key=True)
    titlecn = models.CharField(db_column='titleCn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    titleen = models.CharField(db_column='titleEn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pricecn = models.DecimalField(db_column='priceCn', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priceen = models.DecimalField(db_column='priceEn', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f2c_dues'


class F2CDuesOrder(models.Model):
    oid = models.AutoField(primary_key=True)
    did = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_dues_order'


class F2CEmailLog(models.Model):
    eid = models.AutoField(primary_key=True)
    tid = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_email_log'


class F2CEsLog(models.Model):
    eid = models.AutoField(primary_key=True)
    types = models.CharField(max_length=50, blank=True, null=True)
    act = models.CharField(max_length=20, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    error_data = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_es_log'


class F2CExhibitionActivities(models.Model):
    ea_id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    cover_pic = models.CharField(max_length=255)
    banner_pic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    form = models.CharField(max_length=100, blank=True, null=True)
    scope = models.CharField(max_length=100, blank=True, null=True)
    host_units = models.CharField(max_length=100)
    help_units = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=1000)
    wp_id = models.CharField(max_length=255)
    lang = models.IntegerField()
    status = models.IntegerField()
    is_updown = models.IntegerField()
    is_delete = models.IntegerField()
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_exhibition_activities'


class F2CFeedback(models.Model):
    fid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contents = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_feedback'


class F2CFollowUriType(models.Model):
    fid = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_follow_uri_type'


class F2CFollowUser(models.Model):
    fid = models.BigAutoField(primary_key=True)
    uri = models.CharField(max_length=50, blank=True, null=True)
    web_uri = models.CharField(max_length=300, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    countryname = models.CharField(db_column='countryName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fid_type = models.IntegerField(blank=True, null=True)
    referer = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_follow_user'


class F2CFollowUserBlacklist(models.Model):
    bid = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_follow_user_blacklist'


class F2CHeader(models.Model):
    hid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    keywords_en = models.CharField(max_length=255, blank=True, null=True)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_header'


class F2CHeaderCopy(models.Model):
    hid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    keywords_en = models.CharField(max_length=255, blank=True, null=True)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_header_copy'


class F2CInfo(models.Model):
    i_id = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    info_number = models.CharField(max_length=8)
    s_id = models.IntegerField()
    r_id = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    status = models.IntegerField()
    is_reading = models.IntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    watch_list = models.CharField(max_length=15)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_info'


class F2CLiveBroadcast(models.Model):
    v_id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    v_code = models.CharField(max_length=17, blank=True, null=True)
    v_channelid = models.CharField(db_column='v_channelId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    v_password = models.CharField(max_length=32, blank=True, null=True)
    v_video_url = models.CharField(max_length=255, blank=True, null=True)
    v_title = models.CharField(max_length=64, blank=True, null=True)
    v_main = models.TextField(blank=True, null=True)
    compere = models.CharField(max_length=128, blank=True, null=True)
    compere_intro = models.CharField(max_length=255, blank=True, null=True)
    product_intro = models.CharField(max_length=255, blank=True, null=True)
    long = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    ppt_file = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    v_type = models.IntegerField()
    is_delete = models.IntegerField()
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'f2c_live_broadcast'


class F2CMerchant(models.Model):
    aid = models.IntegerField()
    title = models.CharField(max_length=104, blank=True, null=True)
    main_business = models.TextField(blank=True, null=True)
    company_info = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_merchant'


class F2CMerchantImages(models.Model):
    mid = models.BigAutoField(primary_key=True)
    aid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    i_sort = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_merchant_images'


class F2CNationalCategoryData(models.Model):
    nid = models.AutoField(primary_key=True)
    areaid = models.IntegerField(unique=True, blank=True, null=True)
    category_data = models.TextField(blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    edittime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_national_category_data'


class F2CNationalPageBase(models.Model):
    nid = models.AutoField(primary_key=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    areaid = models.IntegerField(unique=True, blank=True, null=True)
    article_cn_url = models.CharField(max_length=255, blank=True, null=True)
    article_cn_description = models.CharField(max_length=1000, blank=True, null=True)
    article_en_url = models.CharField(max_length=255, blank=True, null=True)
    article_en_description = models.CharField(max_length=1000, blank=True, null=True)
    gold_aid = models.CharField(max_length=1000, blank=True, null=True)
    edittime = models.DateTimeField(blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_national_page_base'


class F2CNav(models.Model):
    nid = models.AutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    chinese = models.CharField(max_length=30, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    english = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_nav'


class F2CNumLimit(models.Model):
    lid = models.AutoField(primary_key=True)
    gid = models.IntegerField()
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    status = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_num_limit'


class F2CPayment(models.Model):
    bill_number = models.CharField(unique=True, max_length=24)
    associator_contact_id = models.IntegerField()
    payment_type_id = models.IntegerField()
    currency_id = models.IntegerField()
    money = models.DecimalField(max_digits=14, decimal_places=2)
    payment_method_id = models.IntegerField()
    buy_time = models.DateTimeField(blank=True, null=True)
    valid_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256)
    is_del = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_payment'


class F2CPaymentMethod(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    name_en = models.CharField(max_length=24)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_payment_method'


class F2CPaymentPayReback(models.Model):
    pid = models.AutoField(primary_key=True)
    associator_contact_id = models.IntegerField()
    bill_number = models.CharField(max_length=24, blank=True, null=True)
    aid = models.IntegerField(blank=True, null=True)
    pp_email = models.CharField(max_length=35, blank=True, null=True)
    pp_first_name = models.CharField(max_length=20, blank=True, null=True)
    pp_last_name = models.CharField(max_length=20, blank=True, null=True)
    paymentid = models.CharField(db_column='paymentId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payer_id = models.CharField(max_length=20, blank=True, null=True)
    pp_user_address = models.CharField(max_length=1000, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_payment_pay_reback'


class F2CPaymentPaypal(models.Model):
    pid = models.AutoField(primary_key=True)
    associator_contact_id = models.IntegerField()
    aid = models.IntegerField()
    pp_email = models.CharField(max_length=35, blank=True, null=True)
    pp_first_name = models.CharField(max_length=20, blank=True, null=True)
    pp_last_name = models.CharField(max_length=20, blank=True, null=True)
    paymentid = models.CharField(db_column='paymentId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payer_id = models.CharField(max_length=20, blank=True, null=True)
    pp_user_address = models.CharField(max_length=1000, blank=True, null=True)
    amount_total = models.FloatField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_payment_paypal'


class F2CPaymentType(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_payment_type'


class F2CProductAttributes(models.Model):
    aid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    weight = models.CharField(max_length=30, blank=True, null=True)
    preservation = models.IntegerField(blank=True, null=True)
    preservation_unit = models.IntegerField(blank=True, null=True)
    intended_for = models.CharField(max_length=30, blank=True, null=True)
    subcommission_clause = models.CharField(max_length=30, blank=True, null=True)
    payment_terms = models.CharField(max_length=30, blank=True, null=True)
    certificate = models.CharField(max_length=50, blank=True, null=True)
    cryopreservation = models.CharField(max_length=30, blank=True, null=True)
    grade = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_product_attributes'


class F2CProductAttributesList(models.Model):
    aid = models.AutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    attributes_cn = models.CharField(max_length=30, blank=True, null=True)
    attributes_en = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_product_attributes_list'


class F2CProductAuditing(models.Model):
    aid = models.AutoField(primary_key=True)
    status = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    pid = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'f2c_product_auditing'


class F2CProductCn(models.Model):
    pid = models.AutoField(primary_key=True)
    aid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    home_description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    areaid = models.CharField(max_length=20, blank=True, null=True)
    catid = models.CharField(max_length=20, blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)
    is_translate = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    is_upper = models.IntegerField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    is_hot = models.IntegerField(blank=True, null=True)
    hot_sort = models.IntegerField(blank=True, null=True)
    is_recommend = models.IntegerField(blank=True, null=True)
    recommend_sort = models.IntegerField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)
    pubdate = models.DateTimeField(blank=True, null=True, auto_now=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_update = models.IntegerField(blank=True, null=True)
    is_en = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_product_cn'


class F2CProductEn(models.Model):
    pid = models.AutoField(primary_key=True)
    aid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    home_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    areaid = models.CharField(max_length=20, blank=True, null=True)
    catid = models.CharField(max_length=20, blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)
    is_translate = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    is_upper = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    is_hot = models.IntegerField(blank=True, null=True)
    hot_sort = models.IntegerField(blank=True, null=True)
    is_recommend = models.IntegerField(blank=True, null=True)
    recommend_sort = models.IntegerField(blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_update = models.IntegerField(blank=True, null=True)
    is_en = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_product_en'


class F2CProductPrice(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    min_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    max_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    min_quantity = models.IntegerField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    moq_unit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_product_price'


class F2CProductUnit(models.Model):
    unit_cn = models.CharField(max_length=255, blank=True, null=True)
    unit_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_product_unit'


class F2CProductsImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_update = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_products_images'


class F2CRole(models.Model):
    rid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_role'


class F2CRss(models.Model):
    rid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    types = models.CharField(max_length=10, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    lang = models.IntegerField(blank=True, null=True)
    cats = models.CharField(max_length=255, blank=True, null=True)
    othermessage = models.CharField(db_column='otherMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contenttype = models.CharField(db_column='contentType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_rss'


class F2CSellForm(models.Model):
    itemid = models.BigAutoField(primary_key=True)
    type_id = models.IntegerField()
    item_number = models.CharField(max_length=13, blank=True, null=True)
    user_id = models.BigIntegerField()
    goods_name = models.CharField(max_length=128, blank=True, null=True)
    cat_id = models.IntegerField()
    son_cat_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    son_area_id = models.IntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    tran_type = models.IntegerField(blank=True, null=True)
    follow_up = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    timeliness = models.IntegerField(blank=True, null=True)
    lasttime = models.DateTimeField()
    addtime = models.DateTimeField()
    end_time = models.CharField(max_length=11, blank=True, null=True)
    is_ch_zn = models.IntegerField(blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_sell_form'


class F2CSellFormEn(models.Model):
    itemid = models.BigAutoField(primary_key=True)
    type_id = models.IntegerField()
    item_number = models.CharField(max_length=13, blank=True, null=True)
    user_id = models.BigIntegerField()
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    cat_id = models.IntegerField()
    son_cat_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    son_area_id = models.IntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    tran_type = models.IntegerField(blank=True, null=True)
    follow_up = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    timeliness = models.IntegerField(blank=True, null=True)
    lasttime = models.DateTimeField()
    addtime = models.DateTimeField()
    end_time = models.CharField(max_length=11, blank=True, null=True)
    is_ch_zn = models.IntegerField(blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_sell_form_en'


class F2CSellImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_number = models.CharField(max_length=13, blank=True, null=True)
    imges = models.CharField(max_length=128, blank=True, null=True)
    imags_sort = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_sell_images'


class F2CSessionCode(models.Model):
    sid = models.BigAutoField(primary_key=True)
    session_id = models.CharField(max_length=32, blank=True, null=True)
    target = models.CharField(max_length=64, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    ct_time = models.CharField(max_length=11, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_session_code'


class F2CShop(models.Model):
    sid = models.AutoField(primary_key=True)
    cid = models.IntegerField(unique=True, blank=True, null=True)
    products_description_en = models.TextField(blank=True, null=True)
    products_description = models.TextField(blank=True, null=True)
    shop_description_en = models.TextField(blank=True, null=True)
    shop_description = models.TextField(blank=True, null=True)
    model_id = models.CharField(max_length=10, blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    sname_en = models.CharField(max_length=255, blank=True, null=True)
    sname = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    aid = models.IntegerField(unique=True, blank=True, null=True)
    domain_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_shop'


class F2CShopAuditing(models.Model):
    aid = models.AutoField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_shop_auditing'


class F2CShopBanner(models.Model):
    bid = models.AutoField(primary_key=True)
    sid = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_shop_banner'


class F2CShopCompanyImages(models.Model):
    img_id = models.AutoField(primary_key=True)
    sid = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    listorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_shop_company_images'


class F2CShopHotProduct(models.Model):
    spid = models.AutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    aid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    listorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_shop_hot_product'


class F2CShopMainProducImages(models.Model):
    img_id = models.AutoField(primary_key=True)
    sid = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    listorder = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_shop_main_produc_images'


class F2CSpecialClassification(models.Model):
    sc_id = models.AutoField(primary_key=True)
    s_id = models.IntegerField(blank=True, null=True)
    sc_cate_pid = models.IntegerField(blank=True, null=True)
    sc_cate_id = models.IntegerField(blank=True, null=True)
    sc_cate_cover_file = models.CharField(max_length=255, blank=True, null=True)
    sc_is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_special_classification'


class F2CSpecialPage(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_type = models.IntegerField(blank=True, null=True)
    s_code = models.CharField(max_length=16, blank=True, null=True)
    s_titile = models.CharField(max_length=128, blank=True, null=True)
    s_banner_cn = models.CharField(max_length=255, blank=True, null=True)
    s_banner_en = models.CharField(max_length=255, blank=True, null=True)
    s_keyword = models.TextField(blank=True, null=True)
    s_status = models.IntegerField(blank=True, null=True)
    s_is_del = models.IntegerField(blank=True, null=True)
    s_release_time = models.CharField(max_length=11, blank=True, null=True)
    s_addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_special_page'


class F2CSpecialProduct(models.Model):
    sp_id = models.BigAutoField(primary_key=True)
    s_id = models.IntegerField(blank=True, null=True)
    sc_cate_id = models.IntegerField(blank=True, null=True)
    sp_pid = models.IntegerField(blank=True, null=True)
    sp_is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_special_product'


class F2CSysconfig(models.Model):
    cid = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_sysconfig'


class F2CTemplet(models.Model):
    tid = models.AutoField(primary_key=True)
    email_title_cn = models.CharField(max_length=255, blank=True, null=True)
    email_content_cn = models.TextField(blank=True, null=True)
    info_title_cn = models.CharField(max_length=255, blank=True, null=True)
    info_content_cn = models.TextField(blank=True, null=True)
    email_title_en = models.CharField(max_length=255, blank=True, null=True)
    email_content_en = models.TextField(blank=True, null=True)
    info_title_en = models.CharField(max_length=255, blank=True, null=True)
    info_content_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_templet'


class F2CVideo(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_code = models.CharField(max_length=17, blank=True, null=True)
    v_compere = models.CharField(max_length=64, blank=True, null=True)
    v_compere_en = models.CharField(max_length=64, blank=True, null=True)
    v_compere_intro = models.CharField(max_length=255, blank=True, null=True)
    v_title_en = models.CharField(max_length=255, blank=True, null=True)
    v_title = models.CharField(max_length=128, blank=True, null=True)
    v_duration = models.CharField(max_length=8, blank=True, null=True)
    v_main = models.TextField(blank=True, null=True)
    v_main_en = models.TextField(blank=True, null=True)
    v_cover = models.CharField(max_length=255, blank=True, null=True)
    v_cover_en = models.CharField(max_length=255, blank=True, null=True)
    v_ppt_file = models.CharField(max_length=255, blank=True, null=True)
    v_ppt_name = models.CharField(max_length=64, blank=True, null=True)
    v_file_url = models.TextField(blank=True, null=True)
    v_status = models.IntegerField(blank=True, null=True)
    v_pay = models.IntegerField(blank=True, null=True)
    v_type = models.IntegerField(blank=True, null=True)
    v_addtime = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2c_video'


class F2CVideoBrowse(models.Model):
    vb_id = models.AutoField(primary_key=True)
    ac_id = models.IntegerField()
    a_id = models.IntegerField()
    v_id = models.IntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f2c_video_browse'


class F2CWonderfulPic(models.Model):
    wp_id = models.AutoField(primary_key=True)
    ea_id = models.IntegerField()
    image_src = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'f2c_wonderful_pic'
