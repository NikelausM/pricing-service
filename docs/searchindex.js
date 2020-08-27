Search.setIndex({docnames:["alert_updater","app","common","controllers","index","libs","models","models.user","modules","templates","views"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["alert_updater.rst","app.rst","common.rst","controllers.rst","index.rst","libs.rst","models.rst","models.user.rst","modules.rst","templates.rst","views.rst"],objects:{"":{app:[1,0,0,"-"],common:[2,0,0,"-"],controllers:[3,0,0,"-"],libs:[5,0,0,"-"],models:[6,0,0,"-"],templates:[9,0,0,"-"]},"common.database":{Database:[2,3,1,""],logger:[2,2,1,""]},"common.database.Database":{AUTHORITY:[2,2,1,"id0"],BASE_HOST_NAME:[2,2,1,"id3"],CONNECTION_OPTIONS:[2,2,1,"id4"],DATABASE:[2,2,1,"id5"],DB_NAME:[2,2,1,"id6"],DB_PASSWORD:[2,2,1,"id7"],DB_USERNAME:[2,2,1,"id8"],HOST:[2,2,1,"id9"],PORT:[2,2,1,"id10"],SCHEME:[2,2,1,"id11"],SCHEME_POST_FIX:[2,2,1,"id12"],URI:[2,2,1,"id13"],USER_INFO:[2,2,1,"id14"],find:[2,4,1,""],find_one:[2,4,1,""],initialize:[2,4,1,""],insert:[2,4,1,""],remove:[2,4,1,""],update:[2,4,1,""]},"common.utils":{Utils:[2,3,1,""]},"common.utils.Utils":{check_hashed_password:[2,4,1,""],email_is_valid:[2,4,1,""],hash_password:[2,4,1,""],random_string_generator:[2,4,1,""]},"controllers.alerts":{"delete":[3,1,1,""],"new":[3,1,1,""],edit:[3,1,1,""],index:[3,1,1,""],logger:[3,2,1,""]},"controllers.stores":{"delete":[3,1,1,""],"new":[3,1,1,""],edit:[3,1,1,""],index:[3,1,1,""],logger:[3,2,1,""]},"controllers.users":{edit:[3,1,1,""],logger:[3,2,1,""],login:[3,1,1,""],logout:[3,1,1,""],register:[3,1,1,""]},"libs.emailer":{Email:[5,3,1,""],EmailException:[5,5,1,""],Encryption:[5,3,1,""],Port:[5,3,1,""],logger:[5,2,1,""]},"libs.emailer.Email":{FROM_TITLE:[5,2,1,"id0"],_ENCRYPTION:[5,2,1,""],_FROM_EMAIL:[5,2,1,""],_FROM_PASSWORD:[5,2,1,""],_PORT:[5,2,1,""],_SMTP_SERVER:[5,2,1,""],send_mail:[5,4,1,""]},"libs.emailer.EmailException":{message:[5,2,1,""]},"libs.emailer.Encryption":{SSL:[5,2,1,"id1"],TLS:[5,2,1,"id2"]},"libs.emailer.Port":{SSL:[5,2,1,"id3"],TLS:[5,2,1,"id4"]},"libs.mailgun":{Mailgun:[5,3,1,""],MailgunException:[5,5,1,""]},"libs.mailgun.Mailgun":{FROM_EMAIL:[5,2,1,"id6"],FROM_TITLE:[5,2,1,"id7"],MAILGUN_API_KEY:[5,2,1,"id8"],MAILGUN_DOMAIN:[5,2,1,""],send_mail:[5,4,1,""]},"libs.mailgun.MailgunException":{message:[5,2,1,""]},"models.alert":{Alert:[6,3,1,""],logger:[6,2,1,""]},"models.alert.Alert":{_id:[6,2,1,""],collection:[6,2,1,"id0"],item:[6,2,1,""],item_id:[6,2,1,"id1"],json:[6,4,1,""],load_item_price:[6,4,1,""],name:[6,2,1,"id2"],notify_if_price_reached:[6,4,1,""],price_limit:[6,2,1,"id3"],user_email:[6,2,1,"id4"]},"models.item":{Item:[6,3,1,""],logger:[6,2,1,""]},"models.item.Item":{_id:[6,2,1,""],collection:[6,2,1,"id5"],json:[6,4,1,""],load_price:[6,4,1,""],price:[6,2,1,"id6"],query:[6,2,1,"id7"],tag_name:[6,2,1,"id8"],url:[6,2,1,"id9"]},"models.model":{Model:[6,3,1,""],logger:[6,2,1,""]},"models.model.Model":{_id:[6,2,1,""],all:[6,4,1,""],collection:[6,2,1,"id10"],find_many_by:[6,4,1,""],find_one_by:[6,4,1,""],get_by_id:[6,4,1,""],json:[6,4,1,""],remove_from_mongo:[6,4,1,""],save_to_mongo:[6,4,1,""]},"models.store":{Store:[6,3,1,""],logger:[6,2,1,""]},"models.store.Store":{URL_PREFIX_REGEX:[6,2,1,"id12"],_id:[6,2,1,""],collection:[6,2,1,"id13"],find_by_url:[6,4,1,""],fix_post_url_prefix:[6,4,1,""],fix_pre_and_post_url_prefix:[6,4,1,""],fix_pre_url_prefix:[6,4,1,""],fix_url_prefix:[6,4,1,""],get_by_name:[6,4,1,""],get_by_url_prefix:[6,4,1,""],json:[6,4,1,""],name:[6,2,1,"id14"],query:[6,2,1,"id15"],tag_name:[6,2,1,"id16"],url_prefix:[6,2,1,"id17"],validate_url_prefix:[6,4,1,""]},"models.user":{decorators:[7,0,0,"-"],errors:[7,0,0,"-"],user:[7,0,0,"-"]},"models.user.decorators":{requires_admin:[7,1,1,""],requires_login:[7,1,1,""]},"models.user.errors":{IncorrectPasswordError:[7,5,1,""],InvalidEmailError:[7,5,1,""],UserAlreadyRegisteredError:[7,5,1,""],UserError:[7,5,1,""],UserNotFoundError:[7,5,1,""]},"models.user.user":{User:[7,3,1,""],logger:[7,2,1,""]},"models.user.user.User":{_id:[7,2,1,""],collection:[7,2,1,"id0"],email:[7,2,1,"id1"],find_by_email:[7,4,1,""],is_login_valid:[7,4,1,""],json:[7,4,1,""],password:[7,2,1,"id2"],register_user:[7,4,1,""]},app:{home:[1,1,1,""],init_db:[1,1,1,""],logger:[1,2,1,""]},common:{database:[2,0,0,"-"],utils:[2,0,0,"-"]},controllers:{alerts:[3,0,0,"-"],stores:[3,0,0,"-"],users:[3,0,0,"-"]},libs:{emailer:[5,0,0,"-"],mailgun:[5,0,0,"-"]},models:{alert:[6,0,0,"-"],item:[6,0,0,"-"],model:[6,0,0,"-"],store:[6,0,0,"-"],user:[7,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","attribute","Python attribute"],"3":["py","class","Python class"],"4":["py","method","Python method"],"5":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:function","2":"py:attribute","3":"py:class","4":"py:method","5":"py:exception"},terms:{"465":5,"587":5,"abstract":[2,6],"case":5,"class":[2,5,6,7],"enum":5,"float":6,"function":[2,7],"int":5,"new":3,"return":[1,2,3,5,6,7],"static":2,"true":[2,6,7],"try":[],For:2,TLS:5,The:[1,2,3,5,6,7],_encrypt:5,_from_email:5,_from_password:5,_id:[6,7],_port:5,_smtp_server:5,abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz:2,about:2,address:5,admin:7,alert:8,alert_id:3,alert_updat:[4,8],all:[2,6],allow:2,allowed_char:2,alreadi:7,also:5,altern:5,ani:6,api:5,app:[4,8],applic:[1,7],assum:2,attribut:6,author:2,avail:5,bad:5,base:[2,5,6,7],base_host_nam:2,been:7,befor:1,behavior:2,being:6,bodi:5,bool:[2,6,7],bson:6,call:6,callabl:7,can:[2,5],charact:2,check:2,check_hashed_password:2,classmethod:[2,5,6,7],client:2,code:2,collect:[2,6,7],colon:2,com:[],combin:5,common:[4,8],compon:2,connect:2,connection_opt:2,consist:2,contain:[2,5,6,7],content:[4,8],control:[4,8],correspond:[2,3,5,6,7],couldn:3,creat:3,css:6,current:6,cursor:2,data:2,databas:[1,6,7,8],dataclass:6,db_base_host_nam:2,db_connection_opt:2,db_name:2,db_password:2,db_port:2,db_scheme:2,db_scheme_post_fix:2,db_schemedb_scheme_post_fix:2,db_usernam:2,decor:[6,8],delet:3,describ:5,desir:6,destroi:3,dict:[2,6,7],displai:5,doc:2,document:2,domain:5,edit:3,either:5,email:[2,6,7,8],email_is_valid:2,emailexcept:5,emailsbi:[],encrypt:[2,5],enumer:5,environ:2,equival:5,error:[5,6,8],except:[5,7],express:6,fail:5,fals:[2,6,7],filter:2,find:[2,6,7],find_by_email:7,find_by_url:6,find_many_bi:6,find_on:2,find_one_bi:6,first:1,fix:6,fix_post_url_prefix:6,fix_pre_and_post_url_prefix:6,fix_pre_url_prefix:6,fix_url_prefix:6,flask:[1,7],format:2,forward:2,found:[6,7],from:[5,6],from_email:5,from_titl:5,further:2,gener:[2,6,7],get:[3,6],get_by_id:6,get_by_nam:6,get_by_url_prefix:6,handl:[3,5],has:[2,5,6,7],hash_password:2,hashed_password:2,hello:[],home:1,host:2,html:[1,5],http:6,human:5,identifi:2,implement:6,incorrect:7,incorrectpassworderror:7,index:[3,4],inform:[1,2,3,5,6,7],init_db:1,initi:[1,2],initvar:[6,7],insert:2,instanc:5,integ:5,intenum:5,interact:2,invalid:[6,7],invalidemailerror:7,is_login_valid:7,item:8,item_id:6,itself:2,json:[6,7],kei:5,latest:[],level:2,lib:[4,8],limit:6,list:[5,6],load:5,load_item_pric:6,load_pric:6,log:[1,2,3,5,6,7],logger:[1,2,3,5,6,7],logic:[2,5],login:[3,7],logout:3,mailgun:8,mailgun_api_kei:5,mailgun_domain:5,mailgunexcept:5,main:1,match:2,maximum:6,merg:5,messag:[5,7],method:[3,6],middlewar:7,mimemultipart:5,model:[3,4,5,8],modul:[4,8],mongodb:6,more:2,multipart:5,name:[2,5,6,7],none:[2,6,7],notifi:6,notify_if_price_reach:6,notimplementederror:6,number:5,object:[2,5,6],objectid:[6,7],onli:7,oper:2,option:[2,5,6],origin:6,otherwis:[2,3,6,7],out:3,packag:[4,8],page:[1,4],paramet:[2,3,5,6,7],pars:6,part:2,pass:7,password:[2,5,7],perform:2,port:[2,5],portion:5,post:[3,5,6],postfix:2,pre:6,preced:2,prefix:6,price:[5,6],price_limit:6,proced:2,protocol:2,provid:[2,6,7],pymongo:2,python:5,queri:[2,6,7],quickstart:[],rais:[3,5,6,7],random:2,random_string_gener:2,reach:6,readabl:5,receiv:5,recipi:5,redirect:3,regex:6,regist:[3,7],register_us:7,remov:[2,6],remove_from_mongo:6,render:5,repli:5,repres:7,represent:[6,7],request:[1,5,6],requires_admin:7,requires_login:7,resourc:2,respons:[3,5,7],rest:3,rout:3,run:[1,2],runtim:2,save:6,save_to_mongo:6,scheme:2,scheme_post_fix:2,script:1,search:4,see:2,selector:6,send:5,send_mail:5,sender:5,separ:5,server:5,servic:5,shown:5,size:2,slash:2,smtp:5,sourc:[1,2,3,5,6,7],specifi:[2,5],ssl:5,start:1,still:5,store:[2,8],store_id:3,store_nam:6,str:[1,2,3,5,6,7],str_size:2,string:[2,5],subcompon:2,subject:5,submodul:8,subpackag:8,successfulli:[5,7],syntax:2,tag:6,tag_nam:6,templat:[3,4,8],text:5,them:5,thi:[1,2,3,5,6,7],thrown:5,tls:5,tri:6,two:[2,5],type:[1,2,3,5,6,7],unfix:6,uniform:2,union:[3,6,7],updat:[2,3],uri:2,url:[2,6],url_prefix:6,url_prefix_regex:6,used:[1,2,3,5,6,7],user:[2,6,8],user_email:6,user_info:2,useralreadyregisterederror:7,usererror:[3,7],usernam:2,usernotfounderror:7,using:5,util:8,valid:[2,6,7],validate_url_prefix:6,valu:[5,6],valueerror:6,variabl:2,verifi:[2,7],version:5,via:6,view:[],web:1,webpag:6,werkzeug:[3,7],when:[5,7],which:6,wiki:2,without:6,wrapper:[3,7]},titles:["alert_updater module","app module","common package","controllers package","Welcome to pricing-service\u2019s documentation!","libs package","models package","models.user package","pricing-service","templates package","views package"],titleterms:{alert:[3,6,10],alert_updat:0,app:1,common:2,content:[2,3,5,6,7,9,10],control:3,databas:2,decor:7,document:4,email:5,error:7,indic:4,item:6,lib:5,mailgun:5,model:[6,7],modul:[0,1,2,3,5,6,7,9,10],packag:[2,3,5,6,7,9,10],price:[4,8],servic:[4,8],store:[3,6,10],submodul:[2,3,5,6,7,10],subpackag:6,tabl:4,templat:9,user:[3,7,10],util:2,view:10,welcom:4}})