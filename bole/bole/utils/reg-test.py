import re
from lxml import etree
text='''<a href="https://www.tepintehui.com/detail/108009?ce" class="avatar" title="这部剧满满的都是周杰伦的回忆杀， 居然还没有炸！">
		    		    	 		    <img src="/img/default_2014.png" data-url="//static.firefoxchina.cn/img/201811/13_5be8d9ca03e960.jpg" class="img-load-delay">
		    		    	 		</a>
			                		<p>
			                		   <a href="https://www.tepintehui.com/detail/108009?ce" title="这部剧满满的都是周杰伦的回忆杀， 居然还没有炸！">
			                		      <span  >这部剧满满的都是周杰伦的回忆杀，<i  >居然还没有炸！</i></span>
			                		   </a>
			                		</p>
			    		    	 </a>
		    		    	 </li>
		    		    	 <input type="hidden" name="_xsrf" value="ahjdfhjkjyu111senashdjk1jhj878" /> 
	    		    		    		    	 		    		    	 <li >
		    		    	 		<a href="https://www.tepintehui.com/detail/108192?ce" class="avatar" title="00后黑话指南， 连90后都搞不明白！">
		    		    	 		    <img src="/img/default_2014.png" data-url="//static.firefoxchina.cn/img/201811/13_5be8d95d4fb270.jpg" class="img-load-delay">
		    		    	 		</a>
			                		<p>
			                		   <a href="https://www.tepintehui.com/detail/108192?ce" title="00后黑话指南， 连90后都搞不明白！">
			                		      <span  >00后黑话指南，<i  >连90后都搞不明白！</i></span>
			                		   </a>
			                		</p>
			    		    	 </a>
		    		    	 </li>


'''

# res = re.findall(r'.*name="_xsrf" value="(.*?)"',text)
# if len(res)>0:
#     print(res[0])

########################################
#print(text)
text2='''<input type="hidden" name="_xsrf" value="ahjdfhjkjyu111senashdjk1jhj878" />
'''

re_obj = re.match(r'^\s*?<input.*name="_xsrf" value="(.*?)"',text2)
#re_obj = re.match(r'.*(yusen).*',text2)
if re_obj:
    print(re_obj.group(1))


res2 = etree.HTML(text).xpath("//input/@value")
print(res2)