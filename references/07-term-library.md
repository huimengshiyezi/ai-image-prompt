# 07 · 词表（AI 绘画提示词库）

> 本文件由 `scripts/render_lexicon.py` 从唯一真源 `lexicon/*.md` 自动生成，**不要手改**。
> 改词请改 `lexicon/` 下的源文件，然后重跑 `python scripts/render_lexicon.py`。

**用法**：用 `scripts/lookup.py` 检索，**不要整份读完** —— 本文件只为检索而生。

共 **1952 条**，12 域 / 40 维度 / 130 要素。

**状态**：常用 1562 · 可用 356 · 少见 13 · 慎用 21　——「慎用」= 有副作用，备注列写明原因，别当普通词用。

---

# ==== 通用层 ====

## 通用-风格

> A · 材料与形式

### 媒介与画种（31）

- 油画 → oil painting
- 丙烯 → acrylic
- 水彩 → watercolor　— 颜色靠纸白透出来，叠色会变深
- 水粉 → gouache　— 不透明水彩，覆盖力强，可与水彩叠用，但不是一回事
- 粉彩 → pastel　— 干性色粉笔直接画，画面偏粉质
- 炭笔 → charcoal　— 比铅笔黑得多、可擦揉，适合铺大关系
- 铅笔 → pencil　— 石墨铅笔，黑白灰，靠笔压出明暗
- 彩色铅笔 → colored pencil　— 不溶于水，靠叠加出层次
- 马克笔 → marker　— 酒精性马克笔，颜色透明、干得快
- 数码绘画 → digital painting　— 笔刷边缘干净
- 数字插画 → digital illustration
- 插画 → illustration
- 儿童插画 → children's illustration
- 纸上彩墨 → color ink on paper　— 颜色透进纸里
- 素描 → sketch　— 快速抓形，不追求完成度
- 水溶彩铅 → watercolor pencil　— 遇水会化开，能画出半水彩的效果
- 蛋彩 → tempera
- 钢笔和墨 → pen and ink　— 蘸水笔或针管笔加墨水，线条锐利
- 墨 → ink
- 喷漆 → spray paint
- 滴漆 → dripping paint　— 颜料直接滴、甩在画布上
- 热蜡 → encaustic　— 加热蜡液作画，表面半透明有厚度
- 中国插图 → Chinese illustration
- 平面插图 → flat illustration
- 写实插画 → realistic illustration　— 写实取向的插画，不是照片
- 混合媒介 → mixed media　— 同时用两种以上材料（如彩铅加水彩、拼贴加丙烯）
- 传统媒介 → traditional media　— 手绘的总称，用来对冲数字感
- 壁画 → fresco　— 画在墙上的画，尺度大、带墙面肌理
- 手稿 → manuscript　— 纸张发黄、有手写痕迹的书页
- 填色本 → coloring book page　— 只有黑线框等着上色
- 线描水彩 → line and wash　— 先勾线再上淡彩

### 东方水墨（21）

- 水墨画 → sumi-e　— 用墨的浓淡干湿表现，不依赖颜色
- 书法 → calligraphy
- 晕染 → ink gradient　— 墨色由浓到淡自然过渡
- 飞白 → dry brush　— 笔速快、墨少，纸上留出一道道白丝
- 淡墨 → light ink wash　— 颜色浅而层次多
- 浓墨 → dense glossy black ink　— 黑得发亮
- 湿笔 → wet brush　— 水分饱满，边缘自然晕开
- 白描 → pure outline　— 只用线画轮廓，不上墨色
- 写意 → abbreviated strokes　— 笔简而意在，不求形似求神似
- 工笔 → fine even lines　— 线条细匀、层层罩染，画得极精细
- 墨色层次 → tonal gradation of ink
- 焦墨 → dense black ink　— 极浓的墨，黑得发亮
- 泼墨 → splashed ink　— 把墨泼在纸上再顺势成画，随机、气势大
- 破墨 → broken ink　— 后一笔破开前一笔，墨色自然渗化
- 积墨 → layered ink　— 一层层叠加，越叠越厚越沉
- 皴法 → texture stroke　— 国画里表现山石纹理的笔法
- 没骨 → no outline　— 不用墨线勾轮廓，直接用色块塑形
- 楷书 → regular script　— 笔画端正
- 行书 → running script　— 笔画之间有牵丝
- 草书 → cursive script　— 连绵不断
- 禅意笔触 → zen brushwork　— 比写意更少，一笔到底、留大量气口

### 版画与印刷（8）

- 木刻 → woodcut　— 在木板上刻出凸版再印，线条有刀味
- 版画 → printmaking
- 蚀刻 → etching　— 用酸腐蚀金属版，线条细而匀
- 石版画 → lithography　— 在石板上画再印，能画出很丰富的调子
- 丝网印刷 → screen printing　— 刮板把墨从网孔挤过去，颜色厚、边界硬
- 凹版印刷 → intaglio　— 墨在凹槽里，压印后线条微微凸起
- 利诺剪裁 → linocut　— 在油毡上刻再印，风格像木刻但更软
- riso 印刷 → risograph　— 孔版印刷，颜色错位、有颗粒、只能叠出有限的几种色

### 立体与工艺（18）

- 雕塑 → sculpture
- 浮雕 → relief　— 图案从底面上凸起来，有厚度和投影
- 马赛克 → mosaic　— 用小色片拼出画面，远看成型、近看是格子
- 纸雕 → paper cut　— 剪出来的图形，边缘利落、有镂空
- 折纸 → origami
- 瓷器 → porcelain　— 高温烧的瓷，白、硬、薄处透光
- 玉 → jade　— 半透明、温润，光进去会散开
- 刺绣 → embroidery　— 用线在布上绣出图案，有丝线的光泽和厚度
- 数字拼贴 → digital collage
- 拼布拼贴 → patchwork collage　— 布料缝在一起，有接缝和厚度
- 卷纸艺术 → paper quilling　— 把纸条卷起来拼成图案
- 彩色玻璃窗 → stained glass　— 铅条把彩色玻璃拼起来，背光透亮
- 挂毯 → tapestry　— 织出来的厚布面，有经纬和绒面
- 金银丝细工 → filigree　— 用极细的金属丝盘成纹样
- 绗缝 → quilted　— 夹层布料缝出线条，表面有起伏
- 纹身图案 → tattoo art　— 皮肤上的图案设计
- 景泰蓝 → cloisonné　— 铜胎掐丝再填珐琅彩，颜色鲜明、有金属边
- 朱红印章 → vermilion seal　— 方形红印，常压在角落

> B · 风格与流派

### 写实程度（11）

- 照片级写实 → photoreal　— 细节密度和真实照片一样
- 超写实 → hyperreal　— 细节比真实照片更多，刻意强化
- 写实 → realistic　— 比例、光影、材质都符合现实，但不必像素级还原
- 半写实 → semi-realistic　— 结构是真的，但能看出是画出来的
- 风格化写实 → stylized realism　— 基底写实，但比例和特征被有意放大
- 卡通化 → cartoonified　— 细节被去掉，只剩大块颜色和明确轮廓
- 高度风格化 → heavily stylized　— 只留最能识别的几个特征，其余全简化
- 极简 → minimal　— 只留最少的信息量
- 抽象化 → abstracted　— 形体被抽掉，只剩轮廓或色块
- 稚拙 → naive　— 比例「错」、线条不规整，但要错得有味道
- 刻意失真 → deliberately off　— 故意画歪比例和透视，制造不安

### 艺术流派（38）

- 文艺复兴 → renaissance
- 巴洛克 → baroque
- 古典主义 → neoclassicism
- 现实主义 → realism
- 印象派 → impressionism
- 野兽派 → fauvism
- 表现主义 → expressionism
- 立体主义 → cubism
- 超现实主义 → surrealism
- 波普艺术 → pop art
- 新艺术 → art nouveau　— 藤蔓般的曲线、花卉纹样、边框装饰
- 装饰性 → ornamental　— 以纹样和重复为主
- 民间艺术 → folk art　— 配色大胆、造型朴素、对称构图
- 蒸汽朋克 → steampunk　— 黄铜、齿轮、皮革、维多利亚
- 赛博朋克 → cyberpunk　— 霓虹、雨夜、高科技低生活
- 合成波 → synthwave　— 八十年代的紫粉荧光、网格地平线
- 复古黑暗 → retro dark vintage　— 七十年代的暗调印刷
- 黑暗幻想 → dark fantasy　— 阴郁、宏大、带哥特与宗教感
- 恐怖 → horror　— 压抑、不安、有威胁感
- 黑色电影 → film noir　— 高对比黑白、百叶窗影、烟与雨
- 涂鸦 → graffiti　— 街头喷绘，字体夸张、颜色冲撞
- 概念艺术 → concept art　— 以交代设定为目的，重结构和设计
- 学院派 → academic art　— 讲究构图、解剖和明暗的古典学院训练
- 浪漫主义 → romanticism
- 点彩派 → pointillism　— 用密集的小色点拼出画面，远看颜色自然混合
- 抽象表现主义 → abstract expressionism
- 未来主义 → futurism　— 用速度线和重复形体表现动感
- 魔幻现实主义 → magic realism
- 批判现实主义 → critical realism
- 欧普艺术 → op art　— 用几何图形制造视觉错觉，画面像在动
- 光色主义 → luminism　— 以光本身为主角，画面通透、发光
- 唯美主义 → aestheticism　— 只为好看，不承担叙事
- 粗野主义 → brutalism　— 暴露混凝土原始质感，粗重、不加修饰
- 建构主义 → constructivism　— 苏联时期海报风格，斜线构图＋红黑配色
- 超现代 → ultra modern　— 极简加金属与玻璃
- 童话风格 → fairy tale style
- 缝隙艺术 → glitch art　— 像素错位与信号故障
- 复古 → vintage　— 十八到十九世纪的旧物感

### 东方风格（5）

- 中国风 → Chinese style
- 国风 → guofeng style　— 当代流行的国潮审美，非严格古风
- 浮世绘 → ukiyo-e　— 日本江户时代的木版画，平涂、勾线、构图奇巧
- 日式风格 → japonism　— 西方视角下的日本趣味，平面、装饰、留白
- 唐卡 → thangka　— 藏传佛教的卷轴画，色彩浓、构图对称、画工极细

### 东方题材（6）

- 武侠 → wuxia　— 侠客、刀剑、江湖气
- 京剧 → Beijing opera　— 脸谱、水袖、靠旗
- 昆曲 → kunqu opera　— 更柔、更素，多用于古典仕女
- 茶艺 → tea ceremony
- 中国童话 → Chinese fairy tale
- 凤凰 → Chinese phoenix　— 东方瑞兽，尾羽拖长、颜色浓

### 动漫游戏（19）

- 日式动画 → anime
- 日本漫画 → manga　— 黑白网点、分镜格、速度线
- 卡通 → cartoon　— 造型简化、轮廓加粗、表情夸张
- 二次元 → ACGN　— 用中文说就是「动漫感」，不必写英文缩写
- Q版 → chibi　— 头大身小的二三头身比例，可爱
- 像素艺术 → pixel art　— 用一个个像素点画出来，边缘是阶梯状的
- 8 比特 → 8-bit　— 八位机画面，色数极少、马赛克大
- 赛璐璐风格 → cel shading　— 颜色分成几个明确的色阶，不渐变
- 卡通渲染 → toon shading　— 3D 模型渲染成 2D 动画的样子，颜色分块、勾黑边
- 三渲二 → 3D cel-shaded　— 用 3D 模型和渲染，做出 2D 手绘动画的观感
- 3D 动画电影 → 3D animated feature　— 造型圆润、材质细腻、光影柔和
- 游戏 CG → game CG　— 高精度的游戏宣传画
- 卡哇伊 → kawaii　— 圆润、甜、无害
- 16 比特 → 16-bit　— 十六位机画面，颜色和分辨率略高
- 90 年代电视游戏 → 90s video game
- 等距卡通渲染 → isometric cel shading　— 等距视角＋卡通渲染，常见于休闲游戏
- 图形小说 → graphic novel　— 成人向的漫画叙事，色调更沉
- 等距动画 → isometric anime
- 魂系 → souls-like　— 灰暗、苍凉、破败的奇幻

### 视觉效果（17）

- 平铺罗列 → knolling　— 物品整齐排列、俯拍
- 拟人化 → anthropomorphic　— 把动物或物体画成人的样子
- 视错觉 → optical illusion
- 扫描线 → scanlines　— 老 CRT 屏幕的横向细线
- 全息投影 → hologram　— 半透明的绿色图像，带扫描线
- X 光透视 → x-ray
- 双重曝光 → double exposure　— 两张画面叠在一张上，互相透出来
- 闪耀效果 → sparkle
- 压缩失真 → jpeg artifacts　— 反复压缩后的方块和马赛克，刻意保留当成风格
- 半调风格 → halftone　— 用大小不同的点模拟连续的明暗，老报纸印刷的做法
- 抖动 → dithering　— 用规律排列的点模拟出中间色，老电脑的渐变做法
- 立体画 → stereogram　— 要眯着眼才看得出
- ASCII 码效果 → ascii art
- 飞溅效果 → splash
- 彩虹反光 → iridescent　— 表面泛出像肥皂泡、油膜那样的多色渐变反光
- 彩色分离 → chromatic separation　— 红蓝通道没能重合，边缘出现红蓝色的重影
- 星闪 → star flash　— 画面里出现十字或四角的星状亮芒，常用来表现高光

### 3D 与渲染（11）

- 3D → 3D render
- 写实 3D 渲染 → photoreal 3D render　— 材质像照片
- 低多边形 → low-poly　— 刻意保留多边形面数，能看见一个个平面
- 黏土渲染 → clay render　— 没有贴图只有形，表面像哑光黏土
- 白模渲染 → white model　— 整体白灰、没有贴图，只看形体和光影
- 全局光照 → global illumination　— 光线在环境里反复弹跳，阴影柔和
- 虚幻引擎 → unreal engine　— 实时渲染，材质厚、辉光强
- 线框渲染 → wireframe render　— 只画模型的网格线，不填面
- 辛烷渲染 → octane render　— GPU 渲染器，干净、光真切、材质准
- 光线追踪 → ray tracing　— 逐条光线计算反射折射，反光和阴影物理正确
- 立体等距 → isometric 3D　— 没有透视的立体，像游戏里的地图

### 平面设计（11）

- 极简主义 → minimalist style
- 扁平化 → flat design　— 无渐变、无阴影、纯色块
- 包豪斯 → bauhaus　— 基本几何形、红黄蓝、无衬线
- 日本海报设计 → Japanese graphic design　— 大量的留白与细字
- 80 年代风格 → 80s style
- 90 年代风格 → 90s style
- 海报排版 → poster layout
- 杂志封面 → magazine cover
- 杂志内页 → magazine spread
- 专辑封面 → album cover
- 街头艺术 → street art　— 喷绘、贴纸、模板印刷

### 摄影风格（18）

- 电影感 → cinematic　— 像电影镜头：明确的方向光、有层次的暗部、克制的色彩
- 电影摄影 → cinematic photography
- 商业棚拍 → commercial studio photography　— 可控布光、纯色或渐变背景
- 人像摄影 → portrait photography　— 背景干净、光比克制
- 时尚摄影 → fashion photography　— 强烈的造型与布光
- 纪实摄影 → documentary photography　— 自然光、不摆拍
- 街拍摄影 → street photography　— 抓拍瞬间
- 静物摄影 → still life photography
- 商品摄影 → product photography　— 白底或浅灰底
- 胶片摄影 → film photography　— 颗粒与微微的偏色
- 胶片颗粒 → film grain
- 剪影照片 → silhouette shot
- 逆光照片 → backlit shot
- 商业摄影 → commercial photography　— 干净、准确、有质感
- 富士色彩 → fujicolor　— 绿青浓郁、肤色偏暖
- 微缩模型电影 → miniature model film　— 布景是模型，景深极浅
- 黑色胶片时期 → pulp noir　— 老黑白印刷的粗颗粒
- 柔焦 → soft focus　— 整张轻微发虚，像雾里看

### 线条（23）

- 线描 → line drawing
- 轮廓线画 → contour drawing　— 只画外轮廓，不画内部结构
- 手势画 → gestural drawing　— 寥寥几笔抓动作，不求准
- 动态速写 → gesture drawing
- 交叉排线 → cross-hatching　— 两组斜线交叉，靠疏密出明暗
- 排线 → hatching
- 剪影画 → silhouette drawing
- 连续线画 → continuous line drawing　— 一笔到底不断线
- 单线画 → single line drawing
- 书法线画 → calligraphic line drawing　— 线条有提按粗细
- 点描 → stippling　— 用密集的小点堆出明暗
- 松散线画 → loose line drawing　— 线不闭合、有重复笔
- 平面线描 → flat line drawing　— 线宽均匀、不表现体积
- 勾勒 → outlining
- 断线画 → broken line drawing　— 线条一段一段断开
- 双线画 → double line drawing　— 每根线都描两遍
- 负空间画 → negative space drawing　— 画的是物体周围的空间
- 紧密线画 → tight line drawing　— 线密到几乎填满
- 角度线描 → angular line drawing　— 全用直线折出形
- 等距线描 → isometric line drawing
- 禅绕画 → zentangle　— 用重复的图案填满一个形状
- 乱画 → scribbling　— 快速、无序、有情绪
- 盲画轮廓 → blind contour drawing　— 只看对象不看纸，形会跑但很有生气

> C · 参照物

### 艺术家（36）

- 达芬奇 → Leonardo da Vinci
- 伦勃朗 → Rembrandt
- 克劳德·莫奈 → Claude Monet
- 梵高 → Van Gogh
- 齐白石 → Qi Baishi
- 伊戈尔·莫尔斯基 → Igor Morski
- 吉卜力 → Studio Ghibli　— 手绘平涂、细节密集、自然光
- 皮克斯 → Pixar　— 圆润造型、明亮材质
- 京都动画 → Kyoto Animation　— 日常系作画、光斑与水的处理精细
- 米开朗基罗 → Michelangelo
- 桑德罗·波提切利 → Sandro Botticelli
- 保罗·塞尚 → Paul Cezanne
- 皮埃尔·奥古斯特·雷诺阿 → Pierre Auguste Renoir
- 瓦西里·康定斯基 → Wassily Kandinsky
- 皮特·蒙德里安 → Piet Mondrian
- 保罗·克利 → Paul Klee
- 吴道子 → Wu Daozi
- 宋徽宗赵佶 → Song Huizong
- 徐悲鸿 → Xu Beihong
- 杰里·平克尼 → Jerry Pinkney
- 梦工厂 → DreamWorks
- 巴勃罗·毕加索 → Pablo Picasso　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 马克·罗斯科 → Mark Rothko　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 萨尔瓦多·达利 → Salvador Dali　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 雷内·马格里特 → Rene Magritte　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 罗伊·利希滕斯坦 → Roy Lichtenstein　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 安迪·沃霍尔 → Andy Warhol　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 草间弥生 → Yayoi Kusama　— 在世艺术家，多数平台禁止指名，建议改用「锚点」描述
- 村上隆 → Takashi Murakami　— 在世艺术家，多数平台禁止指名，建议改用「锚点」描述
- 岳敏君 → Yue Minjun　— 在世艺术家，多数平台禁止指名，建议改用「锚点」描述
- 吴冠中 → Wu Guanzhong　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 张大千 → Zhang Daqian　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 赵无极 → Zao Wou-Ki　— 仍在版权期（逝世未满 70 年），商用请自行评估
- 马特·科利肖 → Mat Collishaw　— 在世艺术家，多数平台禁止指名，建议改用「锚点」描述
- 宫崎骏 → Hayao Miyazaki　— 在世创作者，多数平台禁止指名，建议改用「锚点」描述
- 新海诚 → Makoto Shinkai　— 在世创作者，多数平台禁止指名，建议改用「锚点」描述

### 锚点（5）

- 一九八二年的东京 → Tokyo, 1982　— 年代锚点：一句话顶五十字，模型会补齐一整套符合那个年代的细节
- 罗杰·迪金斯式的打光 → lighting in the style of Roger Deakins　— 创作者锚点：单光源、剪影、大面积暗部
- 一九五七年的哈瓦那 → Havana, 1957　— 年代锚点
- 苏联构成主义海报 → Soviet constructivist poster　— 文化锚点
- 阿什·索普式的电影级体积光 → cinematic volumetric light, Ash Thorp style　— 风格锚点

### 摄影机与胶片（9）

- 香港电影漂白旁路的低饱和 → Hong Kong bleach-bypass, low saturation　— 港风、武侠
- 柯达 200T 的暖橙怀旧胶片色 → warm orange Kodak Vision3 200T　— 复古、怀旧
- ARRI 的色彩科学 → ARRI REVEAL colour science　— 文艺、诗意
- Log-C 冷调去饱和 → Log-C cool desaturated　— 惊悚、悬疑
- 三十五毫米定焦的古典电影感 → shot on a 35mm prime, classic cinematic　— 焦距比摄影机型号更有效的写法
- 用 IMAX 15/70 胶片拍摄 → shot on IMAX 15/70 film　— 史诗、宏大
- 索尼 Venice 2 的青绿冷调 → shot on Sony Venice 2, teal-cool　— 赛博、硬科幻
- 战地纪录片的自然光加灰调 → documentary Log flatness with natural light　— 纪录、战地
- 超十六毫米的高对比偏绿粗粝感 → Super 16mm high-contrast greenish grain　— 恐怖、粗粝

### 年代（7）

- 古代 → ancient
- 二十世纪八十年代 → 1980s
- 老照片 → old photograph　— 褪色、四角发黄、有划痕
- 史前 → prehistoric
- 冰河时代 → ice age
- 侏罗纪 → jurassic
- 十九世纪 → 1800s

## 通用-光线

> A · 布光

### 光位（13）

- 逆光 → backlighting　— 光源在主体背后、镜头对着光拍；主体偏暗，靠边缘光或补光提亮
- 伦勃朗光 → Rembrandt light　— 灯在斜上方 45°，暗侧脸颊上留一个倒三角的光斑，古典人像的经典布光
- 四分之三前光 → three-quarter front light　— 最安全的中性光位
- 侧光 → side light　— 戏剧性、悬疑、黑色电影；最能揭示质感
- 四分之三背光 → three-quarter back light　— 情感场景、深度叙事
- 从后场打光 → light from the back of the set　— 电影布光的首选原则；前场打光会拍成证件照
- 分割光 → split lighting　— 主光从侧面 90° 打，脸正好一半亮一半暗，中间一条直线
- 蝴蝶光 → butterfly lighting　— 灯在正前方偏上，鼻子下面留一个小小的蝴蝶形阴影
- 环形光 → loop lighting　— 影子从鼻侧绕到嘴角，形成一个圈
- 底光 → underlighting　— 从下往上打，反着自然光的方向，不安
- 顶光 → toplighting　— 光从正上方下来，眼窝和下颌陷进阴影，正午户外就是这个效果
- 前光 → frontal light　— 多数情况要避免；只有刻意要高调时尚时才用
- 正后方背光 → full back light　— 梦境、回忆、神圣感

### 灯光类型（28）

- 电影灯光 → cinematic lighting　— 像电影镜头那样打光：有明显方向、有明暗层次、暗部不死黑
- 自然光 → natural light　— 太阳或天光，方向随时间变
- 影棚光 → studio lighting　— 灯光被完全控制，背景干净
- 手机屏幕的光 → phone screen light　— 从下往上照脸，冷白
- 钨丝灯 → tungsten　— 暖黄，暗部偏橙
- 闪光灯 → direct flash　— 硬、直接、边缘清晰
- 荧光灯 → fluorescent lighting　— 偏绿偏冷、让人显得疲惫
- 霓虹灯 → neon lamp　— 管子的颜色映在墙面和皮肤上
- 聚光灯 → spotlight　— 一束打在主体上，周围压暗
- 舞台灯 → stage spotlight　— 一束追光把主体从黑里拎出来
- 重点照明 → accent lighting　— 在主体上单独打一小束光把它「拎」出来，周围压暗
- 三点式照明 → 3-point lighting　— 主光定调＋补光提暗部＋轮廓光勾边，三盏灯各管一件事
- 柔和照明 → soft lighting　— 反差低、过渡软，人像和生活方式图的默认选择
- 低调照明 → low-key lighting　— 画面大部分是暗的，亮部只占一小块，戏剧性最强
- 高调照明 → high-key lighting　— 画面大部分是亮的，几乎没暗部，干净、轻快、商业感
- 穆迪照明 → moody lighting　— 整体压暗、只留少量亮部，情绪压抑、有故事感
- 气氛照明 → atmospheric lighting　— 不为看清主体、只为烘托情绪的辅助光
- 环境光 → ambient light　— 没有明确方向、垫底的底光
- 烛光 → candlelight　— 色温很低，暗部全是暖橙
- 篝火 → firelight　— 光在跳，人物一半亮一半暗
- 月光 → moonlight　— 冷、弱、方向不定
- 阳光直接照射 → direct sunlight　— 影子边缘锐利、方向明确
- 关键照明 → key lighting　— 只靠一盏主光造型，明暗对比强、气氛戏剧化
- 激励照明 → motivated lighting　— 光源在画面里有合理出处（窗、灯、火）
- 双性照明 → bisexual lighting　— 品红＋蓝＋紫三色打光，夜店感的冷艳
- 音乐会照明 → concert lighting　— 彩色光束从后场扫过
- 夜总会照明 → nightclub lighting
- 车灯 → headlights sweeping past　— 一条强光扫过

### 光质（6）

- 硬光 → hard light　— 冷硬、戏剧性、揭示质感与轮廓
- 软光 → soft light　— 柔和、美化、减少瑕疵
- 光比大 → high lighting ratio　— 亮部和暗部的亮度差；光比大＝对比强、戏剧化
- 光比小 → low lighting ratio　— 亮部和暗部的亮度差；光比小＝平、柔和，暗部也留得住细节
- 柔光箱贴着主体 → softbox close in　— 光几乎没有方向
- 反光板补光 → bounce light with a reflector　— 日间外景控光

### 照明风格（5）

- 冷光 → cold light　— 偏蓝青的光，冷静、疏离、科技感
- 暖光 → warm light　— 偏橙黄的光，亲密、怀旧、安全
- 色光 → colored light　— 用带颜色的灯打光，一张图里常配两三种互补色
- 赛博朋克光 → cyberpunk light　— 霓虹的品红＋青蓝对撞，暗部压深、亮部是彩色光源
- 均匀平光 → flat even lighting　— 正面均匀打亮、几乎没有阴影，适合角色设定图和产品图

### 影调（5）

- 高反差 → high contrast　— 亮部和暗部都压到极端，中间调很少，硬朗、有力
- 低反差 → low contrast　— 亮暗差别小，整张发灰，柔和但容易显得脏
- 明暗对比 → chiaroscuro　— 靠明暗交界的强烈对比塑造体积
- 暗部留住细节 → shadows holding detail　— 暗的地方还能看出形状和层次，不是一整块黑
- 高光留住细节 → highlights holding detail　— 最亮的地方还能看出纹理，不是一片白

> B · 光效

### 光线效果（22）

- 边缘光 → edge light　— 从侧后方打的一道窄光，只勾出主体的边，用来把主体从背景里「切」出来
- 发光边 → glowing rim　— 轮廓外面有一圈柔和的亮光，把主体从背景里拎出来
- 强边缘光 → strong rim light
- 荧光 → glowing light　— 物体自己发出柔和的光
- 发光 → glowing　— 光源周围有一圈扩散的亮晕
- 生物发光 → bioluminescent　— 生物自己发光，多为青绿或幽蓝
- 温暖光辉 → warm glow
- 柔和主光配清晰边缘光和自然的接触阴影 → soft key light with a crisp rim light and a natural contact shadow　— 棚拍三件套一起写，缺一个就像渲染图
- 深色底配一个荧光强调色 → a dark ground with one fluorescent accent
- 发光眼睛 → glowing eyes
- 闪闪发光的瞳孔 → sparkling pupils
- 微光 → shimmering light
- 明亮高光 → bright highlights
- 仙气缭绕 → ethereal mist　— 雾状光晕，适合仙侠与神话题材
- 电光闪烁 → electric flash
- 黑光 → blacklight　— 紫外灯下荧光物质发亮
- 紫外线 → ultraviolet
- 荧光棒 → glow stick
- 频闪灯 → strobe light
- 放射性发光 → radioactive glow　— 危险的青绿色自发光
- 熔岩的光芒 → lava glow　— 橙红自下而上的热光
- 核废料的光芒 → nuclear waste glow　— 诡异的黄绿

### 体积光（6）

- 体积光 → volumetric light　— 光被介质挡住一部分，现出一条条可见的光路
- 光柱 → light shafts through mist　— 光穿过雾气形成一道道光柱
- 空气里的浮尘 → dust motes in the light　— 光柱里的尘埃颗粒被照亮，画面有颗粒感
- 丁达尔效应 → tyndall effect　— 光穿过雾、烟或胶体时现出光路，就是常说的「耶稣光」
- 逆光下的蒙蒙亮 → backlit haze　— 空气本身被照亮，整片发亮发白
- 细密水雾散光 → fine spray scattering　— 水雾把光打散，没有明确光路，只有一片柔亮

> C · 环境

### 时间（13）

- 黄金时刻 → golden hour　— 日出后、日落前那一小段，太阳很低、光呈金色，人像和风景最常用
- 蓝调时刻 → blue hour　— 太阳刚落或将升的那段，天是深蓝的，和暖色的人造光对比很好看
- 清晨 → early morning　— 天刚亮，空气里有一层薄雾
- 晨光 → morning light　— 太阳刚出来那阵，光偏暖、角度低、影子长
- 正午顶光 → noon light from straight above　— 太阳在正上方，影子几乎踩在脚下、边缘锐利
- 黄昏 → late afternoon　— 太阳压得很低，一切镀上金边
- 日落 → sunset　— 太阳正在落下，光金黄、云被染红
- 夜晚 → night　— 天已全黑，靠人造光源照亮
- 深夜 → deep night　— 环境全暗，只有一盏灯把主体拎出来
- 日出前后的十分钟 → the ten minutes around sunrise　— 太阳在地平线附近，天从粉过渡到紫，色温变化最快的一小段
- 凌晨 → pre-dawn　— 日出前那段，光是冷青灰色，低对比、很安静
- 硬光打出一块明确的影子，像正午 → hard light throwing one definite shadow
- 清晨或傍晚的自然光 → early morning or late afternoon natural light　— 户外场景产品

### 天气（17）

- 晴天 → clear sky　— 通透的蓝天，光有明确方向，影子颜色偏蓝
- 多云 → cloudy　— 云层遮住太阳，光是漫射的、方向不明显
- 阴天 → overcast　— 云把太阳整个盖住，光是漫射的、几乎没有影子
- 雾 → fog　— 空气里悬浮着小水滴，远处的东西变淡、变灰
- 雾天的光被漫射开 → fog diffusing the light　— 雾把光散开，远处的景物一层层变淡
- 细雨 → light rain　— 雨很细，逆光下能看见一丝一丝的雨
- 大雨 → heavy rain　— 雨很大，雨线连成一片、地面溅起水花
- 雨天 → rainy day　— 在下雨，空气湿、地面反光
- 雨后初晴 → just after rain　— 雨刚停，空气干净，颜色饱和、锐度高
- 暴风雨 → thunderstorm　— 风雨交加，云很厚很黑
- 闪电 → lightning　— 天空里一道分叉的强光
- 小雪 → light snow　— 雪很小，只稀疏地飘几片
- 大雪 → heavy snow　— 雪片很大，被光一照像在翻飞
- 雪后反光 → snow bouncing light from below　— 雪地把光反射上来，下巴和眼窝被从下往上补亮
- 沙尘天气 → dust turning the light orange　— 空气里全是沙尘，光被滤成橙黄，太阳变成一个可直视的圆盘
- 梦幻雾气 → dreamy haze　— 比雾更柔、更亮，像做梦
- 暴雨前的闷光 → the flat glare before a storm　— 暴雨将至，云很低很重、光发闷、色温偏绿灰

## 通用-色彩材质

> A · 色彩

### 基础色（16）

- 红 → red
- 橙 → orange
- 黄 → yellow
- 绿 → green
- 青 → cyan　— 蓝绿之间的颜色，中文里既可指蓝也可指绿（如「青天」「青草」）
- 蓝 → blue
- 紫 → purple
- 粉 → pink　— 介于红和洋红之间，最常见的柔色
- 棕 → brown
- 灰 → grey
- 黑 → black
- 白 → white
- 金 → gold　— 金属感的黄，靠反光和明暗表现
- 银 → silver　— 金属感的灰白，比灰更亮、带反光
- 炭色 → charcoal grey　— 接近黑的深灰，比纯黑柔和、不死板
- 青绿色 → teal　— 蓝绿的中间色，像孔雀石或浅海

### 经典色（11）

- 克莱因蓝 → Klein blue　— 法国艺术家克莱因注册的「国际克莱因蓝」，极高纯度的群青，几乎发光
- 中国红 → Chinese red　— 带一点橙的正红，传统喜庆色
- 普鲁士蓝 → Prussian blue　— 十八世纪德国发明的深蓝颜料，偏冷的暗蓝
- 祖母绿 → emerald　— 浓艳的绿，带一点蓝
- 酒红 → burgundy　— 深红带紫，像红酒
- 玫瑰金 → rose gold　— 粉调的金属金，柔和、偏女性化
- 象牙白 → ivory　— 带一点黄的暖白，比纯白柔和
- 奶茶色 → milk tea　— 米白到浅棕的一组暖中性色，温柔、甜而不腻
- 丹宁蓝 → denim blue　— 牛仔布的靛蓝，从浅到深，日常、耐看
- 孔雀绿 → peacock green　— 像孔雀羽毛的蓝绿，深沉华贵
- 只此青绿 → turquoise green　— 出自舞蹈诗剧《只此青绿》，从《千里江山图》取的青绿

### 色彩属性（18）

- 灰度 → greyscale　— 只有黑到白的深浅，没有颜色
- 黑白 → black and white　— 只保留明暗，去掉所有颜色
- 单色 → monotone　— 整张只有一个色相，靠明度变化
- 明亮色 → bright　— 整体偏亮的配色
- 彩色的 → colorful　— 正常上色，不做黑白处理
- 鲜艳的 → vivid colors　— 高饱和、高识别度的颜色
- 甜 → soft pastel　— 高明度低饱和，清透
- 高饱和 → saturated　— 颜色尽量不掺灰，鲜艳、抢眼
- 低饱和 → desaturated　— 颜色都掺灰，柔和、耐看、高级
- 淡色调 → tints　— 高明度低饱和，清淡、透气
- 颜色怀旧的 → nostalgia　— 低饱和、偏黄或偏青，像旧照片
- 互补色对撞 → complementary colors　— 色环上正对的两个颜色各占一半，强烈、有张力
- 三色均衡 → three colours at 60/30/10　— 三个颜色按 60/30/10 分配，主色定调、点缀色提神
- 强对比配色 → strong contrasting colours　— 演出／派对海报
- 两色系统 → a two-colour system　— 一深一浅
- 多色彩搭配 → multi color　— 四种以上的颜色同时出现，热闹但要控住比例
- 高饱和撞色 → high-saturation clash　— 故意用不协调的高饱和颜色对撞，做出冲击或廉价感
- 琥珀色调 → amber tone　— 像琥珀一样的暖黄棕，怀旧、温暖

### 配色方案（27）

- 莫兰迪色系 → Morandi palette　— 所有颜色都掺了灰，低饱和、安静、高级
- 马卡龙色系 → macaron palette　— 高明度低饱和的甜色（粉、薄荷、鹅黄）
- 糖果色系 → candy palette　— 高饱和高明度的甜色，像水果硬糖
- 大地色系 → earth tones　— 土黄、赭石、橄榄、砖红这一组，自然、耐看
- 日暮色系 → sunset palette　— 紫、橙、粉的过渡色，像黄昏的天空
- 秋日棕色系 → autumn brown　— 秋天落叶的棕黄
- 柔和粉色系 → soft pink　— 低饱和的粉，温柔
- 薄荷绿 → mint green　— 浅绿带一点蓝，清凉
- 珊瑚色 → coral　— 粉和橙交界的暖色，活泼但不刺眼
- 紫罗兰 → violet　— 偏蓝的紫
- 土耳其蓝 → turquoise　— 土耳其石那种蓝绿，异域感
- 霓虹色调 → neon accents　— 品红＋青蓝的高饱和霓虹配色，赛博感
- 黑金色调 → gold and black　— 大面积黑＋金色点缀，奢华感
- 红黑色调 → red and black　— 红加黑，强烈、危险、有力量
- 敦煌色系 → Dunhuang palette　— 敦煌壁画取色：土红、石青、赭石、金，厚重沉稳
- 孟菲斯色系 → Memphis palette　— 八十年代孟菲斯设计小组：高饱和撞色＋几何图形
- 蒙德里安色系 → Mondrian palette　— 红黄蓝三原色＋黑白灰，来自蒙德里安的格子画
- 韦斯·安德森式的配色 → Wes Anderson palette　— 高饱和的粉黄蓝绿，对称、平面、刻意
- 米白纸底配赤陶橙与墨绿 → cream paper with terracotta and deep green
- 纯黑纯白加一个信号色 → pure black and white with one signal colour
- 低饱和的胶片褪色感 → faded desaturated film look
- 鲜果色系 → fresh fruit palette　— 柑橘、莓果那种鲜亮多汁的颜色，清爽
- 枫叶红 → maple red　— 秋天枫叶的橙红
- 雪山蓝 → snow mountain blue　— 高原天空那种冷而透的蓝
- 马蒂斯色系 → Matisse palette　— 野兽派马蒂斯：高饱和平涂色块，大胆、装饰性强
- 洛可可色系 → rococo palette　— 十八世纪法国宫廷风：粉、薄荷绿、金，甜腻繁复
- 冷调单色打底 → a cold monochrome base　— 整体冷灰，只在关键处给一点暖

### 配色方法（6）

- 橙蓝分离 → orange and teal　— 暖橙的主体压在冷蓝的环境里；注意别让肤色变橙
- 漂白旁路 → bleach bypass　— 把漂白步骤跳过，饱和度降低但对比保留，画面发灰发狠
- 单色相不同明度 → a single hue separated only by value　— 整张只有一个颜色，靠深浅区分层次，最稳的配色法
- 一点亮色打破整体的灰 → one bright accent in an all-grey field　— 整张低饱和，只留一个鲜艳的颜色当视觉落点
- 大面积留白 → mostly empty　— 只在关键处上色
- 渐变只用在背景 → gradient only in the background　— 前景元素保持单色

> B · 材质

### 材料（44）

- 玻璃 → glass
- 陶瓷 → ceramic　— 高温烧制的陶或瓷，硬、有釉
- 大理石 → marble　— 白色基底带灰或金的纹路，高档、冷感
- 清水混凝土 → fair-faced concrete　— 拆模后不加任何装饰的混凝土，留着模板缝和螺栓孔
- 不锈钢 → stainless steel　— 工业感、现代感，反光清楚
- 黄铜 → brass　— 比金色沉稳，用久了会有包浆
- 古铜 → antique bronze　— 氧化后的铜，暗棕带绿锈
- 铜 → bronze
- 铝合金 → aluminum
- 碳纤维 → carbon fiber　— 黑色编织纹理，又轻又硬，运动感、科技感
- 耐候钢 → weathering steel　— Corten 钢：特意让它生锈，锈层反而保护内部，颜色是深锈红
- 石材 → stone
- 砂岩 → sandstone　— 颗粒感明显的沉积岩，粗糙、暖色
- 砖块 → brick
- 钻石 → diamond
- 松木 → pine　— 浅色、木纹清楚、有节
- 木制的 → wooden
- 布料 → fabric
- 亚麻布 → linen　— 天然纤维，有粗细不匀的横竖纹理
- 棉质 → cotton
- 天鹅绒 → velvet　— 绒面深、吸光，颜色显得浓
- 缎面 → satin　— 像缎子一样，反光柔和、有丝绸的垂感
- 蕾丝 → lace　— 镂空的花纹网眼
- 皮革 → leather
- 纸张 → paper
- 宣纸 → xuan paper　— 中国书画用纸，吸水、有纤维感
- 珐琅 → enamel　— 在金属上烧一层玻璃质釉，颜色鲜艳、表面光硬
- 塑胶 → plastic
- 箔 → foil　— 极薄的金属膜，反光刺眼、有折痕
- 氧化黄铜 → oxidised brass　— 黄铜氧化后的样子，暗金里泛绿，有年头感
- 镍 → nickel　— 冷银色金属，比铬柔
- 竹钢 → densified bamboo　— 把竹条浸胶高压成型，硬度接近钢，色深
- 玄武岩 → basalt　— 深灰近黑、有细密气孔
- 石英 → quartz　— 半透明、有冷光
- 紫水晶 → amethyst　— 紫色的透明晶体，有内反射
- 乌木 → ebony　— 极黑的硬木，密度大、几乎看不出纹理
- 纱线 → yarn　— 纺成的线，能看见纤维的捻向
- 尼龙 → nylon
- 纸板 → cardboard
- 薄纸巾 → tissue paper
- 光纤 → fiber optic
- 腐朽衰败的 → decayed　— 长了霉斑、起了皮的材料
- 骨骼状 → skeletal
- 菌丝 → mycelium　— 菌丝长成的有机材料，浅色、多孔

### 表面质感（41）

- 金属质感 → metallic　— 有金属的反射和明暗对比
- 拉丝 → brushed　— 表面有平行的方向性纹理，反光被拉长
- 抛光 → polished　— 把表面磨到像镜子一样亮
- 高光洁度 → high polish　— 像镜子一样光滑，能反射出周围环境的形状
- 镜面高光 → specular highlight　— 光滑表面上那一点又小又亮的反光，位置固定、边缘利落
- 磨砂 → frosted　— 表面被打磨成细小颗粒，透光但不透形
- 磨砂玻璃 → frosted glass　— 玻璃被打磨成哑面，光能进来但看不清后面
- 喷砂 → sandblasted　— 高压砂粒打出的均匀哑面
- 哑光 → matte　— 不反光，表面只有暗淡的反射
- 绒面 → suede　— 有细密绒毛的表面，反光是散开的
- 毛绒质感 → fluffy　— 表面立着细密的绒毛，反光散开
- 皮毛质感 → fur texture　— 动物毛皮，有方向和深浅变化
- 针织质感 → knitted　— 毛线织出来的，有针脚的凹凸
- 绸缎质感 → silk texture　— 反光柔和、有方向和垂感
- 珠光质感 → pearl luster　— 反光柔和且带一点颜色偏移
- 玻璃质感 → glass texture　— 透明、有厚度感，边缘会折射
- 水晶质感 → crystal texture　— 透明且折射强，内部有光路
- 半透明 → translucent　— 光能透过去，但看不清后面的东西
- 透明质感 → clear transparency　— 边缘清晰
- 玻璃的通透与厚边的绿 → clear glass with the green of a thick edge　— 玻璃透光，但厚的地方会泛出青绿色
- 塑料质感 → plastic texture　— 表面均匀、反光软，没有材质肌理
- 皮革质感 → leather texture
- 皮革的毛孔与压线 → leather grain and stitching
- 镀铬 → chrome　— 表面像镜子一样反光，周围环境被完整映出来
- 金属漆质感 → metallic paint　— 油漆里掺了金属粉，有细密的闪烁颗粒
- 雕刻质感 → carved texture　— 表面有刻出来的凹凸，靠阴影成型
- 竹子质感 → bamboo texture　— 有节、有纵向纤维的浅色硬质
- 织物纹理 → warp and weft　— 能看见经纬的交织
- 湿润的表面 → moist　— 表面挂着一层水膜，反光被拉长
- 表面凝结着细密的水珠 → fine beads of condensation　— 低温表面挂的一层细密水珠
- 油光在表面形成亮点 → specular highlights from the oil　— 油膜把光聚成小亮点
- 高光过渡 → highlight rolloff　— 亮部到中调过渡柔和、不过曝
- 真实的反射 → genuine reflections
- 水面倒影 → water reflection
- 露珠 → dew drops
- 皮肤是哑光的 → matte skin　— 只有高光处反光，不是整片油光
- 褶皱质感 → wrinkled　— 表面布满不规则的折痕
- 内部折射 → internal refraction　— 透明物体内部的光线弯折，出现亮线和错位
- 油漆质感 → paint texture　— 刷过漆的表面，有刷痕或厚薄
- 水波纹质感 → water ripple　— 表面像水面一样有同心或平行的波纹
- 石墨质感 → graphite texture　— 铅笔那种灰黑色带金属反光

## 通用-镜头构图

> A · 取景

### 景别（28）

- 极限特写 → extreme close-up　— 比特写还近，只留眼睛或嘴这样的局部
- 脸部特写 → detail shot (ECU)　— 只拍脸，背景几乎看不到，情绪最直接
- 头部特写 → headshot　— 从头顶到下巴，比脸部特写略松一点
- 头部以上 → big close-up (BCU)　— 头顶到画面上边还留一点空间
- 胸部以上 → medium close-up (MCU)
- 腰部以上 → waist shot
- 七分身 → three-quarter shot　— 影视里最常用的对话景别，能同时看清表情和手势
- 膝盖以上 → knee shot
- 全身 → full length shot
- 半身像 → bust
- 肖像 → portrait
- 中景 → medium shot (MS)
- 中远景 → medium long shot (MLS)
- 宽景 → wide view
- 景观 → an expansive view　— 一片完整的环境，主体在其中
- 全景照片 → panorama　— 超宽画幅、能看到大片环境
- 超广角 → ultra wide shot　— 比广角更极端，画面边缘明显变形，适合拍空间和冲击力
- 微距 → macro shot　— 凑到极近拍，能看到肉眼看不到的纹理
- 两景 → two shot　— 画面里正好两个人，多用于对话戏
- 群景 → group shot　— 一群人全在画面里，看清谁站哪儿
- 俯拍平铺 → flat-lay from above　— 相机在正上方垂直向下，像把东西摊在桌上拍
- 人占四分之三 → long shot　— 主体占画面约四分之三，留一点空间但不空
- 人在远方 → extra long shot (ELS)　— 人很小，环境为主
- 微观 → microscopic view　— 显微镜级别的放大
- 松散景 → loose shot　— 画面留很多余地，主体不占满，呼吸感强
- 近距离景 → tight shot　— 画框卡得很紧
- 三景 → three shot　— 画面里正好三个人
- 横截面图 → cross-section view

### 视角（30）

- 平视 → eye-level　— 相机与视线等高，最平实、最不带评价
- 正面 → front view　— 正对着主体，最直接、最对称
- 侧面 → profile　— 从侧面拍，能看清轮廓线
- 侧视图 → side view
- 背视图 → back view
- 仰视 → look up　— 从下往上看，被拍的人显得强大、有压迫感
- 俯视 → top view　— 从上往下看，被拍的人显得弱小、被观察
- 水平视角 → horizontal view angle
- 四十五度斜俯 → a 45-degree downward angle　— 最常用的一档
- 鸟瞰图 → aerial view　— 从很高的地方往下看，能看到大片地面布局
- 等距视角 → isometric　— 没有透视的近失，所有平行线保持平行
- 交错视角 → Dutch angle　— 画面刻意歪斜，制造不安
- 肩膀视角 → over the shoulder　— 越过一个人的肩膀拍另一个人，带出两者关系
- 第一人称视角 → first-person view　— 镜头就是角色的眼睛，代入感最强
- 第三人称视角 → third-person perspective　— 镜头在角色之外观察，观众是旁观者
- 产品视图 → product view
- 平视（与标签等高） → a level angle at label height　— 产品图常用
- 看向观众 → looking at viewer　— 主体直视镜头，打破第四面墙，有交流感
- 电影角度 → cinematic angle　— 像电影镜头那样取景：有意识的角度、不追求「拍全」
- 摄影机对准人物的视线 → camera on the eyeline　— 视角谱系的高认同端
- 摄影机偏离视线四十五度 → camera 45 degrees off the eyeline　— 最常用的叙事视角
- 卫星视图 → satellite view　— 垂直向下、接近地图的读法
- 底视图 → bottom view
- 反转视角 → reverse angle
- 自由视角 → free camera
- 固定视角 → fixed camera
- 跟随视角 → follow camera
- 随意视角 → arbitrary view
- 摄影机离视线更远 → camera far off the eyeline　— 中立旁观，认同感最低
- 内视镜视角 → endoscopic view

### 设定图与多视图（8）

- 角色设定图 → character design sheet
- 角色三视图 → character turnaround sheet
- 角色四视图 → character four-view sheet
- 三视图站姿 → three-view neutral stance　— 三个角度都用同一个中性站姿，方便比对
- 前视、侧视、后视图 → front, side, rear view
- 面部特写格 → face close-up panel　— 多视图里单开一格画头部特写
- 立绘 → character illustration　— 单人、全身、姿态讲究
- 转面图 → character turnaround

> B · 构图

### 构图（28）

- 三分法 → rule of thirds　— 把画面横竖各分三等份，主体放在交叉点或线上，最稳的构图法
- 黄金分割 → golden ratio　— 按 1:1.618 切分画面，比三分法更「自然」的比例
- 中心构图 → centered composition
- 对称构图 → symmetrical composition
- 非对称构图 → asymmetrical composition
- 对角线构图 → diagonal composition
- 水平线构图 → horizontal line composition
- 横向构图 → horizontal composition　— 画面横向展开，适合风景和群像
- 三角构图 → triangular composition　— 三点连成三角形，画面最稳；倒三角则制造不稳定
- S 形构图 → S-shaped composition　— 主体或引导线走成 S 形，视线顺着走完全图
- 引导线 → leading lines　— 用画面里的线条（路、栏杆、光）把视线引向主体
- 消失点构图 → vanishing point composition　— 所有线条朝一个点收拢，纵深和空间感最强
- 框架式构图 → frame composition　— 用门、窗、树枝等在前景框住主体，做出纵深
- 负空间构图 → negative space composition　— 主体周围留大片空白，靠「空」突出主体
- 焦点构图 → focal point composition　— 把最亮或最清楚的一点放在关键位置，视线自然落过去
- 重复构图 → repetition composition　— 同样的形状反复出现，形成节奏
- 重叠构图 → overlapping composition　— 前后物体相互遮挡，靠遮挡关系表达层次
- 遮挡构图 → blocking composition　— 用前景的物体挡住一部分主体，制造层次和窥视感
- 对比构图 → contrast composition　— 把两个相反的东西并置（大／小、明／暗、冷／暖）
- 布景构图 → mise-en-scene　— 场景里的每样东西都为叙事服务
- 并列构图 → juxtaposition　— 把两件不相关的东西并排放，靠反差说话
- 散点构图 → scattered composition
- 剪影构图 → cut out composition　— 主体压成黑色轮廓，形状本身成为主体
- 径向构图 → radial composition　— 元素从中心向外辐射，视线被拉向圆心
- 动态对称 → dynamic symmetry
- 分割互补构图 → split complementary composition
- 拼贴构图 → collage composition　— 把不相关的画面拼在一张里，打破单一空间
- 线条构图 → line composition

### 透视（6）

- 一点透视 → one-point perspective　— 正对着走廊、马路、铁轨拍；最基础也最有力的纵深做法
- 两点透视 → two-point perspective　— 两个消失点，像站在街角看建筑的两个面
- 三点透视 → three-point perspective　— 三个消失点，多加一个垂直方向的，俯仰看高楼用
- 立面透视 → elevation perspective　— 正对建筑的一个面拍，透视被压平、线条横平竖直
- 空气透视 → aerial perspective　— 远景一层层变淡、变蓝，画远景必备
- 广角变形 → wide-angle distortion　— 24mm 以下明显；靠近画面边角的脸和物体都会变形

> C · 光学

### 焦距（16）

- 鱼眼镜头 → fisheye lens　— 视野接近甚至超过 180°，画面四周拉成圆弧
- 广角镜头 → wide-angle lens　— 通常指焦距小于 35mm 的镜头，可捕捉更广阔的场景
- 长焦镜头 → telephoto lens　— 通常指焦距大于 70mm 的镜头，可拍摄远距离的主体
- 微距镜头 → macro lens　— 可拍摄极其细小的主体，通常有 1:1 的放大倍率
- 定焦镜头 → prime lens
- 长焦压缩 → telephoto compression　— 200mm 以上明显；前后景像贴在同一个平面上
- 二十四毫米 → 24mm　— 空间感和冲击力强，靠近边缘的物体会被拉长
- 三十五毫米 → 35mm　— 略广但不夸张，街头和纪实最常用
- 五十毫米 → 50mm　— 最接近人眼看到的比例，不变形、最自然
- 八十五毫米 → 85mm　— 脸不容易变形，背景压缩柔和；对人像最有效
- 一百毫米微距 → 100mm macro　— 退得够远不挡光
- 镜头贴近，浅景深 → shot close with shallow depth of field　— 材质微距
- 移轴镜头 → tilt-shift lens　— 镜头能平移或倾斜，把真实场景拍出「微缩模型」的错觉
- 变焦镜头 → zoom lens
- 一百三十五毫米 → 135mm　— 背景压得更扁、虚化更浓，主体更突出
- 两百毫米以上 → 200mm and beyond　— 前后景几乎贴在一起，背景化成一片

### 光圈（7）

- f/1.4 → f/1.4　— 景深很浅、焦外光斑很大很圆
- f/1.8 → f/1.8　— 便宜定焦的常见规格，虚化够用、画质比全开好一档
- f/2.8 → f/2.8　— 虚化明显但主体还在焦内，工作和生活照的常用档
- f/5.6 → f/5.6　— 多数镜头收两档后最锐，同时还留一点虚化
- f/8 → f/8　— 从前景到背景基本都清楚，风光和产品的常用档
- f/1.2 → f/1.2　— 只有眼睛那一层清楚，其余全化开
- f/16 → f/16　— 整张都锐，但可能出现衍射导致画质下降

### 焦外（11）

- 背景虚化 → shallow depth of field bokeh
- 奶油一样化开的焦外 → creamy, fully dissolved bokeh　— 虚化的背景过渡极其柔和，没有硬边
- 圆形的光斑 → round bokeh balls　— 虚化出来的光点是正圆的
- 前景 → foreground　— 靠近镜头、通常被虚化的一层元素，用来做纵深
- 前后景同时虚化 → foreground and background both soft　— 只有主体实
- 背景完全融成一片色块 → the background melted into flat colour
- 猫眼焦外 → cat's-eye bokeh　— 画面边缘的光点被镜头口径挡住，压成橄榄形
- 旋焦 → swirl bokeh　— 焦外的光斑沿一个方向旋转，画面有眩晕感（老镜头特征）
- 焦外像水彩一样晕开 → bokeh dissolving like watercolour
- 焦外有明显方向性的拖影 → directional smear in the out-of-focus areas　— 像在移动
- 二线性焦外 → busy bokeh　— 多数情况是缺陷，除非刻意要粗糙感

### 对焦与光学（11）

- 景深 → depth of field　— 画面里「看起来清楚」的那一段前后距离；越浅虚化越强
- 焦点对准 → in focus　— 焦点明确落在主体上，主体锐利
- 专注于脸 → focus on face　— 焦点锁在脸上，其余都化开
- 聚焦在 → focus on
- 前置焦点 → foreground focus　— 焦点落在靠近镜头的前景上，主体反而在后面虚着
- 晕影 → vignetting　— 画面四角比中间暗，像透过一个暗角看进去
- 色差 → chromatic aberration　— 镜头没把不同颜色的光聚到同一点，物体边缘出现红蓝彩边
- 防抖 → image stabilization　— 画面稳、没有手持的抖动感
- 快门速度 → shutter speed　— 感光的时间长短：越快越能凝固动作，越慢越容易糊
- 感光度 → ISO　— ISO：对光的敏感程度，越高越亮但噪点越多
- 高动态范围 → HDR　— 亮部和暗部同时保留细节

### 相机类型（9）

- 全画幅相机 → full-frame camera　— 传感器大小等同于 35mm 胶片
- 中画幅相机 → medium format camera　— 可拍摄更高分辨率和更细腻的细节
- 数码单反相机 → DSLR　— 有反光镜和光学取景器，续航好、手感稳
- 无反相机 → mirrorless camera　— 没有反光镜，取景靠电子屏，机身更薄
- 数码相机 → digital camera
- 胶片相机 → film camera　— 用胶卷成像，有颗粒和独特的色彩，不能立刻回看
- 莱卡相机 → Leica
- APS-C 画幅相机 → crop sensor camera　— 传感器小于全画幅
- 傻瓜相机 → point-and-shoot camera　— 小、快、随手拍

### 曝光参数（6）

- 曝光不足 → underexposed　— 整体偏暗，暗部细节被压掉，情绪低沉
- 曝光过度 → overexposed　— 整体偏亮，最亮处变成纯白、失去细节
- 低感光度 → low ISO　— 画质最干净，需要足够的光
- 低光照片 → low-light shot
- 向右曝光 → expose to the right　— 在不过曝的前提下尽量往亮曝，后期拉回时暗部更干净
- 高感光度 → high ISO　— 有可见颗粒，常用于暗光和纪实感

### 运动（12）

- 动态模糊 → motion blur　— 物体在曝光期间移动，留下拖影
- 体现运动的线 → motion lines　— 用线条画出运动的轨迹
- 速度线 → speed lines　— 用线条画出运动的方向和速度
- 追随拍摄 → panning　— 相机跟着主体移动拍，主体实、背景拉成横线
- 慢门拖出长长的运动模糊 → a slow shutter trailing long motion blur
- 长曝光把车灯拉成一条条光轨 → a long exposure turning lights into trails
- 慢门拍流水 → a slow shutter turning water into silk　— 水面变成丝绸
- 主体有轻微动态模糊 → slight motion blur on the subject only　— 背景是实的
- 头发和衣角被风带起来 → hair and hems lifted by the wind
- 定格在动作最高点的一瞬 → frozen at the apex of the movement
- 星轨 → star trails　— 超长曝光几十分钟，星星转成一圈圈弧线
- 抖动的画面 → a jittery frame　— 刻意保留手持的抖动，纪录片和抓拍感

## 通用-背景收尾

> A · 背景

### 背景（7）

- 纯色背景 → solid color background
- 白色背景 → white background
- 背景为深色纯色 → a solid dark background that separates the subject cleanly　— 主体干净分离
- 渐变的背景 → gradient background
- 模糊背景 → blurred background
- 简单背景或无背景 → simple or no background
- 透明背景 → transparent background　— 需要后期合成时用

> B · 收尾

### 收尾（5）

- 画面里只有主体 → only the subject　— 没有别的东西进来
- 画面里只有一个人 → only one person in the frame　— 防「减法错」：不写模型容易自己加人
- 画面里不要出现任何文字 → no text anywhere in the image
- 画面干净 → a clean frame with no background clutter　— 不要有杂乱的背景物件
- 镜面反射里不要出现杂物 → no clutter in reflections

### 排除项（9）

- 不要添加随机文字、乱码或水印 → no random text, gibberish or watermarks　— 几乎所有图都该写
- 不要生成二维码、电话、地址或证书 → do not generate QR codes, phone numbers, addresses or certificates　— 这类细节模型必出错，交给后期
- 不要添加假的标志或假的赞助商 → no fake logos or fake sponsors
- 不要添加不存在的配件 → no accessories that do not exist　— 产品图专项
- 不要过度饱和 → avoid oversaturation　— 食品图尤其
- 不要添加虚假折扣或虚假承诺 → no fake discounts or claims
- 不要出现真实艺人姓名或票务信息 → no real artist names or ticketing details　— 演出海报
- 不要生成标题或按钮文字 → leave out headline and button text so the image can be typeset later　— 官网首屏
- 不要过度锐化 → avoid over-sharpening

# ==== 题材层 ====

## 人像

> A · 人物基础

### 主体类型（29）

- 女性 → female
- 男性 → male
- 女孩 → girl
- 男孩 → boy
- 女仆 → maid
- 修女 → nun　— 天主教女性修行者，穿黑白修道服
- 巫女 → miko　— 日本神道教的女性神职人员，穿白衣红袴
- 魔法少女 → magical girl　— 普通女孩变身成有法力的战士
- 女巫 → witch　— 西方奇幻里的施法女性，常配尖帽与扫帚
- 法师 → mage
- 忍者 → ninja　— 黑衣、蒙面
- 天使 → angel
- 恶魔 → demon
- 吸血鬼 → vampire
- 幽灵 → ghost
- 美人鱼 → mermaid
- 精灵 → elf　— 小体型、尖耳朵的奇幻种族
- 妖精 → fairy　— 带翅膀的小型奇幻生物
- 怪物 → monster
- 人偶 → doll　— 像玩偶一样的人，通常表情空洞、关节可见
- 医生 → doctor
- 护士 → nurse
- 教师 → teacher
- 啦啦队 → cheerleader　— 运动场边加油的队伍
- 兽人 → beastfolk　— 人和兽的混合种族
- 服务员 → waiter
- 伪娘 → crossdressing
- 女巨人 → giantess
- 迷你少女 → minigirl

### 年龄段（6）

- 儿童 → a child　— 大约六到十二岁
- 少年 → a teenager　— 大约十三到十七岁
- 青年 → a young adult in their twenties　— 二十多岁
- 中年 → a middle-aged person in their forties　— 四十到五十岁
- 老年 → an elderly person over sixty　— 六十岁以上
- 幼儿 → a toddler　— 大约三到五岁

### 面孔特征（7）

- 东亚面孔 → East Asian features
- 欧美面孔 → Caucasian features
- 混血面孔 → mixed-race features
- 非裔面孔 → African features
- 南亚面孔 → South Asian features
- 中东面孔 → Middle Eastern features
- 拉丁裔面孔 → Latina features

> B · 五官

### 脸型（14）

- 鹅蛋脸 → oval face
- 圆脸 → round face
- 方脸 → square face
- 长脸 → long face
- 心形脸 → heart-shaped face　— 尖下巴、额头宽
- 婴儿肥 → baby fat　— 脸颊有肉
- 颧骨高 → high cheekbones with hollowed cheeks　— 脸颊微凹
- 下颌线清晰 → a sharply defined jawline
- 尖下巴 → a pointed chin
- 面部轮廓柔和 → soft facial contours
- 面部轮廓硬朗 → hard, angular facial contours
- 菱形脸 → diamond face　— 颧骨最宽
- 下颌角明显 → a pronounced jaw angle
- 圆下巴 → a rounded chin

### 眼睛（15）

- 杏眼 → almond eyes　— 圆而略长
- 丹凤眼 → phoenix eyes　— 细长、内眼角往下
- 狐狸眼 → fox eyes　— 眼尾挑得很高
- 圆眼 → round eyes　— 睁得很开
- 细长眼 → narrow eyes
- 吊眼角 → tsurime　— 外眼角往上吊，有攻击性或东方感
- 下垂眼 → tareme　— 外眼角往下走，显得无辜、柔和
- 双眼皮 → double eyelid
- 单眼皮 → single eyelid
- 内双 → hidden double eyelid
- 眼窝深 → deep-set eyes
- 卧蚕 → aegyo-sal　— 眼下那一条微微鼓起的肉
- 水汪汪的眼睛 → watery eyes　— 眼里含着一层水光
- 眼距宽 → wide-set eyes
- 眼距窄 → close-set eyes

### 眼睛颜色（13）

- 棕色眼睛 → brown eyes
- 蓝色眼睛 → blue eyes
- 绿色眼睛 → green eyes
- 灰色眼睛 → grey eyes
- 紫色眼睛 → purple eyes
- 红色眼睛 → red eyes
- 金色眼睛 → golden eyes
- 琥珀色眼睛 → amber eyes
- 橙色眼睛 → orange eyes
- 粉色眼睛 → pink eyes
- 多色眼睛 → multicolored eyes
- 渐变瞳色 → gradient eyes
- 恶魔眼 → devil eyes　— 瞳色发红发光、带异样神采

### 瞳孔（15）

- 爱心瞳 → heart-shaped pupils
- 星形瞳孔 → star-shaped pupils
- X 形瞳孔 → x-shaped pupils
- 符号形瞳孔 → symbol-shaped pupils
- 竖瞳 → slit pupils　— 像猫一样
- 异色瞳 → heterochromia
- 空白瞳孔 → blank pupils　— 没有高光，像空洞
- 瞳孔扩张 → dilated pupils
- 星星眼 → sparkling eyes　— 瞳孔里画着星星，表示极度期待或崇拜
- 钻石形瞳孔 → diamond-shaped pupils
- 一字型瞳孔 → horizontal pupils
- 蛇瞳 → snake pupils
- 恶魔瞳 → devil pupils
- 纽扣眼 → button eyes　— 像布偶
- 瞳孔收缩 → constricted pupils

### 眼睛状态（13）

- 眨眼 → wink
- 睁大眼睛 → wide-eyed
- 眯起眼睛 → narrowed eyes
- 闭上眼睛 → closed eyes
- 一只眼睛闭着 → one eye closed
- 半闭眼睛 → half-closed eyes
- 翻白眼 → rolling eyes
- 睁着眼落泪 → crying with eyes open
- 眼下痣 → mole under eye
- 黑眼圈 → dark circles
- 眼圈发红 → ringed eyes　— 刚哭过
- 布满血丝的眼睛 → bloodshot eyes
- 斗鸡眼 → cross-eyed

### 睫毛（7）

- 睫毛 → eyelashes
- 长睫毛 → long eyelashes
- 浓密的睫毛 → thick lashes
- 卷翘的睫毛 → curled lashes
- 睫毛膏 → mascara　— 睫毛根根分明
- 彩色睫毛 → colored eyelashes
- 下睫毛清晰 → lower lashes clearly visible

### 眉毛（19）

- 浓眉 → thick brows
- 细眉 → thin brows
- 柳叶眉 → willow-leaf brows　— 弧度柔和
- 剑眉 → straight brows　— 眉尾上扬有力
- 平眉 → flat brows
- 弓形眉 → arched brows
- 上挑眉 → upswept brows
- 野生眉 → untamed brows　— 没修过、毛流感强
- 修过的眉 → groomed brows　— 边缘干净利落
- 皱眉 → frown
- 挑眉 → raised eyebrows
- 单边挑眉 → one brow lifted　— 只挑起一边
- 眉头微蹙 → brows slightly drawn together
- V 形眉 → v-shaped brows
- 下垂眉 → downturned brows
- 八字眉 → splayed brows
- 银色眉毛 → silver brows
- 白色眉毛 → white brows
- 无眉 → browless　— 特殊设定

### 鼻型（10）

- 鼻梁挺拔 → a straight, high nose bridge
- 鼻梁低平 → a low, flat nose bridge
- 鼻头圆润 → a rounded nose tip
- 鼻头小巧 → a small, neat nose tip
- 鼻尖微微上翘 → a tip that turns up slightly
- 鼻翼窄 → narrow nostrils
- 侧面看鼻子是一条直线 → a straight nose in profile
- 鼻梁有驼峰 → a bridge with a slight hump
- 鹰钩鼻 → an aquiline nose
- 鼻翼宽 → wide nostrils

### 耳型（16）

- 耳垂明显 → visible earlobes
- 贴面耳 → ears close to the head
- 招风耳 → ears that stick out
- 小巧的耳朵 → small ears
- 耳廓清晰 → a clearly drawn ear shell
- 耳尖微红 → ear tips faintly flushed
- 尖耳 → pointy ears
- 猫耳 → cat ears
- 狐耳 → fox ears
- 犬耳 → dog ears
- 兔耳 → rabbit ears
- 狼耳 → wolf ears
- 熊耳 → bear ears
- 鹿耳 → deer ears
- 虎耳 → tiger ears
- 鼠耳 → mouse ears

### 嘴部与牙齿（27）

- 张口 → open mouth
- 闭嘴 → closed mouth
- 嘴唇微张 → parted lips
- 努嘴 → pout
- 撅起的嘴唇 → puckered lips
- 咬牙 → clenched teeth
- 吐舌头 → tongue out
- 舔嘴唇 → licking lips
- 虎牙 → fangs
- 露出虎牙 → fang out
- 露出上排牙齿 → upper teeth
- 厚唇 → full lips
- 薄唇 → thin lips
- 上唇薄、下唇厚 → a thin upper lip over a fuller lower
- 唇峰明显 → a defined cupid's bow
- 唇珠饱满 → a full lip bead
- 小巧的唇 → a small mouth
- 嘴角上扬 → corners turning up
- 嘴角下垂 → corners turning down
- 唇色偏红 → lips on the red side
- 唇色偏淡 → lips pale
- 朱唇 → red lips
- 唇釉反光 → glossy lips　— 唇珠有明显亮点
- 挡住嘴巴 → covering mouth
- 手放在嘴边 → hand to mouth
- 宽唇 → a wide mouth
- 嘴唇有干裂的细纹 → fine chapping on the lips

### 皮肤质感（8）

- 皮肤有真实的毛孔和细纹 → real pores and fine lines　— ⭐ 不写容易出塑料脸
- 鼻尖和额头有一点自然的油光 → a little natural oil on nose and forehead
- 颧骨上有几颗雀斑 → a few freckles across the cheekbones
- 皮肤下有淡淡的血色透出来 → a faint flush under the skin
- 颈部和锁骨处的皮肤更薄更亮 → thinner, brighter skin at neck and collarbone
- 细小的绒毛被侧光照亮 → fine down lit by the side light
- 眼下有淡淡的青色与细纹 → faint shadow and fine lines under the eyes
- 出汗后的湿润感 → a slight sheen of sweat

> C · 表情与情绪

### 正面情绪（24）

- 微笑 → smile
- 浅笑 → light smile
- 温柔的微笑 → kind smile
- 露齿而笑 → grin
- 得意地笑 → smirk
- 坏笑 → evil smile
- 苦笑 → sad smile
- 憋笑 → stifled laugh
- 正在笑 → laughing　— 眼睛弯起来
- 对视一笑 → exchanging a smile
- 兴奋 → excited
- 快乐 → happy
- 期待 → hopeful
- 欣喜若狂 → elated
- 脸红的 → blush
- 害羞 → shy
- 尴尬害羞 → embarrassed　— 眼神飘向一边
- 可爱脸 → cute face
- 不安的微笑 → nervous smile
- 强迫笑 → forced smile
- 疯狂的笑 → crazy smile
- 用手指做出笑脸 → finger smile
- 得意脸 → doyagao
- 迷人的微笑 → seductive smile　— 偏性感，注意平台规则

### 负面情绪（35）

- 悲伤 → sad
- 忧郁 → gloom　— 整个人往下沉，肩膀塌、视线低
- 沮丧 → frustrated
- 苦恼 → annoyed
- 生气 → angry
- 气愤 → upset
- 一脸不悦 → unamused
- 厌恶 → disgust
- 轻蔑 → disdain
- 怒视 → scowl
- 害怕 → fearful
- 恐惧 → horrified
- 不安 → anxious
- 恐慌 → panicking
- 绝望 → despair
- 孤独 → lonely
- 嫉妒 → envy
- 邪恶 → evil
- 哭泣 → crying　— 眼眶发红
- 啜泣 → sobbing
- 要哭的表情 → tearing up
- 忍着的表情 → endured face
- 闷闷不乐 → sulking　— 不说话、嘴角往下
- 脸色阴沉 → shaded　— 眼神往下压
- 情绪压着 → depressed　— 嘴角绷紧不说话
- 疲惫 → tired
- 傲娇 → tsundere　— 嘴上凶、心里在意
- 不安地抿嘴 → nervous　— 手指绞在一起
- 烦躁 → fume　— 漫画里头顶冒烟
- 疼痛 → pain
- 尖叫 → screaming
- 叹气 → sigh
- 病娇 → yandere　— 因为爱而走向偏执与危险
- 嚣张 → troll　— 张扬、目中无人
- 厌恶的怪相 → grimace

### 疑问与惊讶（5）

- 惊讶 → surprised
- 疑惑 → confused
- 恍惚 → torogao
- 惊讶到掉色 → color drain　— 极端符号化表达
- 无语 → spit take

### 中性表情（4）

- 面无表情 → expressionless
- 认真 → serious　— 嘴唇抿成一条线
- 思考 → thinking
- 沉思 → pensive

### 眼神（10）

- 凝视 → staring
- 眼神坚定 → determined　— 下颌收紧
- 眼神放空 → bored
- 失望地垂眼 → disappointed
- 心虚地移开视线 → guilt
- 轻蔑的眼神 → jitome　— 半垂眼、斜看
- 眼神乱飘 → flustered
- 盯着你 → stare at me　— 直视镜头
- 眼神斜过去 → jealous
- 眼中闪现强烈的情感 → glint

### 哭泣（5）

- 眼泪 → tears
- 流泪 → streaming tears
- 开心的眼泪 → happy tears
- 眼眶含着泪没落下来 → eyes brimming
- 泪痕 → tear stains

### 面部反应（7）

- 困倦 → sleepy　— 快睁不开
- 醉酒 → drunk
- 失神 → unconscious
- 瞳孔放大（受惊） → scared
- 憋气 → holding breath
- 喘粗气 → heavy breathing
- 闻 → smelling

### 面部动作（9）

- 以手掩面 → facepalm
- 鼓着腮帮 → cheek bulge
- 捏脸颊 → cheek pinching
- 戳脸颊 → cheek poking
- 抬下巴 → chin grab
- 遮住眼睛 → covering eyes
- 挡住脸 → covering face
- 扯脸颊 → cheek pull
- 蒙住眼睛 → covered eyes

> D · 毛发

### 发色（19）

- 黑发 → black hair
- 棕发 → brown hair
- 浅褐发 → light brown hair
- 金发 → blonde hair
- 红发 → red hair
- 银发 → silver hair
- 白发 → white hair
- 灰发 → grey hair
- 粉发 → pink hair
- 蓝发 → blue hair
- 紫发 → purple hair
- 绿发 → green hair
- 渐变发色 → gradient hair
- 挑染 → streaked hair
- 多色头发 → multicolored hair
- 内侧染色 → colored inner hair
- 深蓝发 → dark blue hair
- 浅蓝发 → light blue hair
- 彩虹发 → rainbow hair

### 发长（5）

- 短发 → short hair
- 长发 → long hair
- 中长发 → medium hair
- 超长发 → very long hair
- 长发及腰 → hair past the waist

### 刘海（14）

- 刘海 → bangs
- 齐刘海 → blunt bangs
- 斜刘海 → slanted bangs
- 中分刘海 → middle-parted bangs
- 分开的刘海 → parted bangs
- 不对称刘海 → asymmetrical bangs
- 交错刘海 → crossed bangs
- 辫子刘海 → braided bangs
- 眼间刘海 → hair between eyes
- 朝一个方向的刘海 → side-swept bangs
- 掀起的刘海 → bangs pinned back
- 头发遮着双眼 → hair over eyes
- 头发遮住一只眼 → hair over one eye
- 美人尖 → widow's peak

### 束发与编发（21）

- 马尾 → ponytail
- 低马尾 → low ponytail
- 高马尾 → high ponytail
- 双马尾 → twintails
- 短双马尾 → short twintails
- 侧马尾 → side ponytail
- 辫子 → braid
- 双辫 → twin braids
- 侧辫 → side braid
- 法式辫 → french braid
- 冠型编发 → crown braid
- 多发辫 → multiple braids
- 脏辫 → dreadlocks
- 发髻 → hair bun
- 丸子头 → topknot
- 双丸子头 → double bun
- 盘发 → updo
- 半扎发 → half updo
- 单侧扎发 → one side up
- 长鬓角 → sidelocks
- 扎头发 → tied hair

### 卷发与直发（7）

- 直发 → straight hair
- 卷发 → curly hair
- 波浪卷 → wavy hair
- 钻发 → drill hair
- 双钻发 → twin drills
- 多钻发 → quad drills
- 外卷发型 → flipped hair

### 发质与状态（13）

- 有光泽的头发 → shiny hair
- 蓬松头发 → big hair
- 湿头发 → wet hair
- 飘动的头发 → floating hair
- 摆动的头发 → hair flaps
- 一缕一缕的发丝 → hair strand
- 散发 → hair spread out
- 披肩发 → hair over shoulder
- 耳后发 → hair behind ear
- 呆毛 → ahoge
- 多根呆毛 → antenna hair
- 云絮状发型 → cloud hair
- 水晶状的头发 → crystal hair

### 短发造型（17）

- 寸头 → buzz cut
- 平头 → crew cut
- 蘑菇头 → bowl cut
- 波波头 → bob cut
- 精灵头 → pixie cut
- 不对称短发 → asymmetrical hair
- 鲻鱼头 → mullet
- 鸟窝头 → afro
- 蜂窝头 → beehive
- 莫霍克 → mohawk
- 玉米编 → cornrows
- 凌乱发型 → messy hair
- 刺刺的头发 → spiked hair
- 秃头 → bald
- 头发后梳 → hair pulled back
- 平顶 → flattop
- 河童头 → okappa

> E · 体型

### 身形（14）

- 苗条 → slim
- 纤细 → slender
- 匀称 → a balanced build
- 健壮 → a sturdy build
- 肌肉发达 → muscular with visible definition
- 娇小 → petite
- 高挑 → tall and slim
- 丰满 → curvy
- 瘦 → thin
- 高 → tall
- 矮 → short
- 小蛮腰 → a small waist
- 大长腿 → long legs
- 胖 → fat

### 肩颈（5）

- 锁骨明显 → prominent collarbones
- 直角肩 → square shoulders
- 颈部修长 → a long neck
- 肩背线条清楚 → a defined shoulder and back line
- 溜肩 → sloping shoulders

### 腰腹（4）

- 腰线明显 → a clear waistline
- 腹肌线条 → abdominal definition
- 腰部曲线 → a curved waistline in profile
- 腰腹紧实 → a flat stomach

### 四肢（4）

- 腿型修长 → slender legs
- 手臂纤细 → slim arms
- 手指细长 → long, slender fingers
- 手部骨感 → bony hands with visible knuckles

> F · 服装

### 上装（27）

- T恤 → T-shirt
- 衬衫 → shirt
- 翻领衬衫 → collared shirt
- 马球衫 → polo shirt
- 毛衣 → sweater
- 连帽毛衣 → hooded sweater
- 露肩毛衣 → off-shoulder sweater
- 卫衣 → hoodie
- 夹克 → jacket
- 连帽夹克 → hooded jacket
- 西装外套 → suit jacket
- 粗呢大衣 → duffel coat
- 外套 → coat
- 背心 → vest
- 无袖紧身背心 → tank top
- 罩衫 → blouse
- 运动衫 → jersey
- 燕尾服 → tailcoat
- 披风 → cape
- 白大褂 → lab coat
- 细肩带 → spaghetti strap
- 露腰上衣 → midriff
- 袖肩分离装 → detached sleeves
- 短袖 → short sleeves
- 长袖 → long sleeves
- 正装 → formal wear
- 袈裟 → kesa

### 裙装（18）

- 裙子 → skirt
- 迷你裙 → miniskirt
- 短裙 → short skirt
- 长裙 → long skirt
- 百褶裙 → pleated skirt
- 紧身裙 → pencil skirt
- 包臀裙 → sheath skirt
- 蓬蓬裙 → pettiskirt
- 泡泡裙 → bubble skirt
- 荷叶边裙 → frilled skirt
- 牛仔裙 → denim skirt
- 格子裙 → checkered skirt
- 高腰裙 → high-waist skirt
- 吊带裙 → suspender skirt
- 女仆裙 → maid apron
- 正装短裙 → skirt suit
- 芭蕾短裙 → tutu
- 超短裙 → microskirt　— 注意平台规则

### 裤装（12）

- 裤子 → pants
- 牛仔裤 → jeans
- 破牛仔裤 → torn jeans
- 牛仔短裤 → denim shorts
- 短裤 → shorts
- 热裤 → hotpants
- 七分裤 → capri pants
- 运动裤 → track pants
- 瑜伽裤 → yoga pants
- 紧身裤 → leggings
- 灯笼裤 → bloomers
- 背带裤 → overalls

### 连身与礼服（13）

- 连衣裙 → dress
- 紧身连衣裙 → bodycon dress
- 毛衣连衣裙 → sweater dress
- 露肩连衣裙 → off-shoulder dress
- 有领连衣裙 → collared dress
- 无袖连衣裙 → sleeveless dress
- 蕾丝边连衣裙 → lace-trimmed dress
- 百褶连衣裙 → pleated dress
- 晚会礼服 → evening gown
- 婚纱 → wedding dress
- 体操服 → leotard
- 开襟连衣裙 → open dress
- 露背连衣裙 → backless dress　— 注意平台规则

### 传统服饰（8）

- 汉服 → hanfu
- 旗袍 → cheongsam
- 唐装 → tang suit
- 和服 → kimono
- 浴衣 → yukata
- 水手服 → sailor uniform
- 学校制服 → school uniform
- 中式礼服 → Chinese formal dress

### 鞋袜（30）

- 运动鞋 → sneakers
- 乐福鞋 → loafers
- 平底鞋 → flat shoes
- 高跟鞋 → high heels
- 细跟高跟鞋 → stiletto heels
- 玛丽珍鞋 → mary janes
- 芭蕾舞鞋 → ballet slippers
- 靴子 → boots
- 马丁靴 → combat boots
- 及膝靴 → knee boots
- 高跟长靴 → high heel boots
- 拖鞋 → slippers
- 短袜 → socks
- 长袜 → knee-high socks
- 过膝袜 → thigh-high socks
- 泡泡袜 → loose socks
- 横条袜 → striped socks
- 丝袜 → stockings
- 黑丝 → black stockings
- 白丝 → white pantyhose
- 网袜 → fishnet stockings
- 损坏的过膝袜 → torn thigh-highs
- 蕾丝裤袜 → lace tights
- 条纹连裤袜 → striped tights
- 女式学生鞋 → uwabaki
- 日式足袋 → tabi
- 腿部系带 → ankle lace-up
- 褶边裤袜 → frilled tights
- 褶边长筒袜 → frilled thigh-highs
- 大腿靴 → thigh boots　— 注意平台规则

### 泳装与内衣（4）

- 泳装 → swimsuit　— 泳装品类；避免人物化呈现
- 连体泳衣 → one-piece swimsuit　— 泳装品类；避免人物化呈现
- 内衣 → underwear　— 电商内衣品类可用；避免人物化呈现
- 比基尼 → bikini　— 泳装品类；注意平台规则

> G · 配饰

### 帽子（28）

- 棒球帽 → baseball cap
- 鸭舌帽 → flat cap
- 渔夫帽 → bucket hat
- 绒线帽 → beanie
- 礼帽 → top hat
- 软呢帽 → fedora
- 贝雷帽 → beret
- 草帽 → straw hat
- 太阳帽 → sun hat
- 头巾 → turban
- 兜帽（放下） → hood down
- 兜帽（戴上） → hood up
- 水手帽 → sailor hat
- 圣诞帽 → santa hat
- 女巫帽 → witch hat
- 法师帽 → wizard hat
- 护士帽 → nurse cap
- 皇冠 → crown
- 头冠 → tiara
- 头顶光环 → halo
- 兽角 → horns
- 鹿角 → antlers
- 龙角 → dragon horns
- 护额 → forehead protector
- 迷你礼帽 → mini top hat
- 派对帽 → party hat
- 东金帽 → tokin hat
- 带翅膀的头盔 → winged helmet

### 发饰（19）

- 发箍 → headband
- 发夹 → hairclip
- 发带 → hair ribbon
- 头绳 → hair tie
- 发圈 → hair scrunchie
- 蝴蝶结发饰 → hair bow
- 簪子 → kanzashi
- 月牙发饰 → crescent hair ornament
- 星星发饰 → star hair ornament
- 心形发饰 → heart hair ornament
- 蝴蝶发饰 → butterfly hair ornament
- 花朵发饰 → flower hair ornament
- 羽毛头饰 → feather hair ornament
- 发珠 → hair beads
- 兽耳头罩 → animal hood
- 女仆头饰 → maid headdress
- 褶边蕾丝发带 → frilled lace headband　— 层叠褶边的蕾丝发带，甜美系
- 猫耳耳机 → cat ear headphones
- 铃铛发饰 → hair bell

### 面部配饰（32）

- 眼镜 → glasses
- 无框眼镜 → rimless eyewear
- 半框眼镜 → over-rim eyewear
- 戴眼镜的 → bespectacled
- 太阳镜 → sunglasses
- 眼罩 → blindfold
- 独眼眼罩 → eyepatch
- 口罩 → face mask
- 医用口罩 → surgical mask
- 拉着口罩 → mask pull
- 面纱 → veil
- 狐狸面具 → fox mask
- 面具（掀到头上） → mask on head
- 摘下的面具 → mask removed
- 护目镜 → goggles
- 头上别着护目镜 → goggles on head
- 无线耳机 → wireless earbuds
- 面纹 → facepaint
- 额前宝石 → forehead jewel
- 额前图案 → forehead mark
- 脸颊上的疤痕 → scar on cheek
- 眼部疤痕 → scar across the eye
- 贴着绷带的脸 → bandage on face
- 用绷带包扎一只眼 → bandage over one eye
- 美人痣 → beauty mark
- 纹身 → tattoo
- 厚如瓶底的圆眼镜 → coke-bottle glasses
- 心形眼镜 → heart-shaped eyewear
- 天狗面具 → tengu mask
- 防毒面具 → gas mask
- 头戴显示设备 → head-mounted display
- 从后脑戴的耳机 → behind-the-head headphones

### 耳饰（6）

- 耳环 → earrings
- 耳钉 → stud earrings
- 环状耳环 → hoop earrings
- 心形耳环 → heart earrings
- 水晶耳环 → crystal earrings
- 长坠耳饰 → long drop earrings

### 颈饰（13）

- 项链 → necklace
- 贴颈项圈 → choker　— 贴颈的窄项圈
- 颈带 → ribbon choker
- 项圈 → collar
- 领带 → necktie
- 领结 → bow tie
- 水手领 → sailor collar
- 围巾 → scarf
- 丝带 → ribbon
- 珠链 → bead necklace
- 首饰 → jewelry
- 锚形项圈 → anchor choker
- 项链挂口哨 → whistle around neck

### 手饰（8）

- 手链 → bracelet
- 手镯 → bangle
- 手表 → wristwatch
- 手套 → gloves
- 长手套 → elbow gloves
- 露指手套 → fingerless gloves
- 蕾丝手套 → lace gloves
- 绷带缠手臂 → bandaged arm

### 腰部与包（8）

- 腰带 → belt
- 腰包 → fanny pack
- 围腰毛衣 → sweater around waist
- 双肩包 → backpack
- 手提包 → handbag
- 斜挎包 → cross-body bag
- 单肩包 → one-shoulder bag
- 帆布包 → canvas bag

### 手持道具（9）

- 雨伞 → umbrella
- 手杖 → cane
- 魔杖 → staff
- 金权杖 → golden staff
- 扇子 → folding fan
- 书 → book
- 花束 → bouquet
- 酒杯 → wine glass
- 左轮手枪 → revolver

> H · 动作与姿态

### 手部动作（37）

- 招手 → waving
- 牵手 → holding hands
- 拥抱 → hug
- 张开双臂 → spread arms
- 双抬臂 → arms up
- 双手叉腰 → hands on hips
- 单手插腰 → hand on hip
- 手交叉于胸前 → arms crossed
- 手放身后 → arms behind back
- 手臂放头后 → arms behind head
- 手插在口袋里 → hands in pockets
- 手自然垂着 → hands hanging naturally
- 手撑着头 → chin rest
- 一手托腮 → one hand propping the chin
- 双手交叠放在膝上 → both hands folded on the lap
- 双手相扣 → hands clasped
- 双手捧住一样东西 → both hands cupping something
- 手指捏着一个小物件 → fingers pinching a small object
- 一只手撩头发 → one hand sweeping the hair
- 双手拨头发 → hands in hair
- 手放脸上 → hand on face
- 手放胸前 → hand on chest
- 翘大拇指 → thumbs up
- 剪刀手 → peace sign　— 食指和中指比 V，最常见的拍照手势
- 攥拳 → clenched fist
- 摸头 → headpat　— 把手放在自己头上，表示困扰或撒娇
- 自拍 → selfie
- 扶正眼镜 → adjusting eyewear　— 用手指把眼镜往上推，常见于斯文形象
- 拳打 → punching
- 敬礼 → salute
- 手枪手势 → finger gun
- 猫爪手势 → cat pose
- 抬起食指 → index finger raised
- 拉头发 → hair pull
- 手腕内侧朝上 → the inner wrist turned up
- 五指张开贴在玻璃上 → a hand splayed flat against glass
- 手指绕着杯沿划圈 → a finger tracing the rim of a cup

### 腿部与站姿（22）

- 站立 → standing
- 坐着 → sitting
- 蹲下 → squatting
- 下跪 → kneeling
- 正坐 → seiza
- 侧身坐 → yokozuwari
- 盘腿 → cross-legged
- 抱腿坐 → knees up
- 双腿并拢 → legs together
- 双腿交叉 → crossed legs
- 双腿分开 → legs apart
- 单腿站立 → standing on one leg
- A 字站姿 → A-pose
- T 字站姿 → T-pose
- 中性站姿 → neutral stance
- 光腿 → bare legs
- 战斗姿态 → fighting stance
- 跨坐 → straddle
- 抬腿 → leg up
- 脚踢 → kicking
- 膝到胸 → knees to chest
- 屈膝礼 → curtsy

### 全身动作（24）

- 身体前倾 → leaning forward
- 躺着 → lying
- 侧躺 → on side
- 趴着 → on stomach
- 仰面躺 → on back
- 睡觉 → sleeping
- 颤抖 → trembling
- 弓起身体 → arched back
- 唱歌 → singing
- 跳舞 → dancing
- 拉伸 → limbering up　— 压腿、扩胸一类准备活动
- 伸懒腰 → a waking stretch　— 双臂上举、身体后仰，刚醒或放松时
- 靠墙 → against wall
- 回头 → looking back
- 抬头 → head tilt
- 背对背 → back-to-back
- 玩水 → wading
- 浸在水中 → partially submerged
- 动态姿势 → dynamic pose
- 正面站姿 → front-facing neutral pose
- 浮在水上 → afloat
- 脚在水里 → soaking feet
- 身体颠倒 → upside-down
- 四肢着地 → all fours

> I · 关系互动

### 关系互动（29）

- 脸贴脸 → cheek-to-cheek
- 额头贴额头 → forehead-to-forehead
- 两个人贴得很近 → two people standing very close　— 肩膀几乎靠在一起
- 二人面对面 → facing another
- 两人对望 → the two looking at each other　— 视线交叉
- 两人朝同一方向看 → both looking the same way
- 共同望向远方 → both looking off to the distance　— 不看对方
- 手牵手 → holding hands with fingers interlaced　— 手指交扣
- 挽着手臂 → arm in arm　— 一个人靠着另一个人
- 一只手搭在对方肩上 → one hand resting on the other's shoulder
- 搂着腰 → an arm around the waist
- 一方从背后环抱另一方 → one embracing the other from behind
- 正面拥抱 → a frontal embrace　— 手臂环住对方
- 摸对方的头 → one hand patting the other's head
- 亲吻额头 → a kiss on the forehead
- 亲吻脸颊 → a kiss on the cheek
- 耳语 → whispering close to the ear　— 凑到耳边说话
- 额头抵着对方的肩膀 → forehead against the other's shoulder
- 母亲低头看孩子 → a mother looking down at her child
- 大人牵着小孩的手 → an adult holding a child's hand
- 背靠背坐着 → sitting back to back
- 并肩走 → walking side by side in step　— 步幅一致
- 一个坐着、一个站在旁边 → one seated, the other standing beside
- 一个人回头 → one turning back　— 另一个在前方
- 高矮差明显 → a clear height difference　— 一高一矮并肩
- 一人前景一人背景 → one figure in the foreground　— 前后错开
- 递给对方一样东西 → handing something over
- 家人围坐 → family seated in a loose circle　— 构成一个圈
- 两人平行站位 → two figures in parallel　— 构图对称

> J · 妆容

### 妆容（6）

- 化妆 → makeup
- 素颜 → bare-faced　— 几乎没有妆感
- 淡妆 → light natural makeup　— 只提气色
- 浓妆 → heavy makeup　— 眼影与唇色都重
- 泪痣 → a beauty mark under the eye
- 晒伤妆 → sunburn blush　— 颧骨横过一道红

## 风景自然

> A · 地貌

### 地形（21）

- 山 → a mountain
- 山谷 → a valley
- 山顶 → a summit
- 悬崖 → a sheer cliff dropping straight down　— 垂直的岩壁直插下去
- 高原 → a plateau
- 平原 → flat plains with a horizon stretched far　— 地平线拉得很平很远
- 草原 → a meadow
- 沙漠 → a desert
- 红土荒漠 → red desert rock eroded into pillars　— 风把红色砂岩蚀成一根根柱子
- 盐湖 → an endless salt flat with a mirror surface　— 水面极平，能完整倒映天空（天空之镜）
- 火山 → a volcano
- 火山口边缘 → the rim of a crater with smoke beyond　— 远处有烟
- 洞穴 → a cave narrowing then opening out　— 岩壁往里收窄然后豁然开阔
- 冰洞穴 → an ice cave
- 冰川裂隙 → a glacier crevasse glowing blue　— 冰层深处的蓝最亮
- 冰原 → an ice sheet　— 一望无际的冰盖，只有风刻出的纹路
- 陡峭的峡谷 → a steep canyon with near-vertical walls　— 两壁几乎垂直
- 陨石坑 → a crater with a raised rim and sunken center
- 外星地貌 → an extraterrestrial landscape　— 不像地球的岩层与颜色，可能是紫或绿的天空
- 地外世界 → an extraterrestrial world
- 潮间带滩涂 → tidal flats with ripples left by the ebb　— 退潮后留下一条条纹路

### 水体（10）

- 大海 → the ocean
- 海面波光 → sunlight shattered across the wave tops　— 阳光在浪尖上碎成一片
- 礁石与浪花 → waves breaking white against rocks　— 浪撞上石头炸开
- 湖 → a lake
- 冰封的湖面 → a frozen lake with bubbles and cracks beneath　— 底下有气泡和裂纹
- 江河 → a broad slow river　— 水面宽而流速慢
- 溪流 → a stream splitting around stones　— 水在石头间分成几股
- 瀑布 → a waterfall with mist at the base　— 水从高处砸下来，底下有水雾
- 沼泽 → still marsh water with duckweed floating　— 水是静的，漂着浮萍
- 水下世界 → an underwater world　— 镜头在水面以下，能看到光柱和水泡

### 植被（15）

- 森林 → a forest
- 针叶林 → a conifer forest　— 松杉类树林，颜色很深、树形是尖塔
- 竹林 → a bamboo grove　— 竿子笔直、叶片细碎
- 白桦林 → birches with black scars on white trunks　— 白树皮上有黑色横疤的树林，北方特征
- 枫树林 → a maple grove turned solid red　— 叶子红成一片
- 高山草甸 → an alpine meadow in sheets of wildflowers　— 高海拔的草地，夏天开满小野花
- 花田 → a flower meadow
- 樱花 → cherry blossoms
- 落花 → falling petals
- 苔藓 → moss wrapping stones and roots in green　— 苔藓长满石头和树根，把一切染绿
- 藤蔓 → vines hanging down and taking over　— 从上面垂下来缠住一切
- 芦苇 → reeds leaning as one when the wind passes　— 芦苇丛被风吹得整片倾斜
- 仙人掌 → columnar cacti standing with spines　— 柱子一样立着、带刺
- 树 → trees
- 花草 → flowers and grass

> B · 天时

### 天象（17）

- 天空 → sky
- 夜空 → night sky　— 天是深的蓝黑色，有层次、不是纯黑
- 星空 → starry sky　— 能看到星星，天很干净、没有光污染
- 月亮 → moon
- 太阳 → sun
- 流星 → shooting star
- 银河 → the Milky Way
- 星云 → nebula
- 极光 → aurora borealis
- 梦幻云彩 → dreamy clouds
- 火烧云 → a sky burned orange at sunset　— 整片天被烧成橘红
- 厚重的积雨云 → heavy cumulonimbus pressing low
- 平流雾 → advection fog creeping along the ground　— 雾像水一样贴着地面流动，把低处淹掉
- 双层彩虹 → a double rainbow
- 雨幡 → virga trailing from the cloud base　— 雨还没落地就在空中蒸发，云底垂下一缕缕丝
- 乳状云 → mammatus bulging under the cloud　— 云底垂下一个个袋状鼓包，暴风雨前后出现
- 日晕 → a solar halo ringing the sun　— 冰晶折射阳光形成的一圈光环

### 季节（10）

- 春 → spring
- 初春 → early spring　— 枝头刚冒出一点嫩绿
- 夏 → summer
- 盛夏 → high summer　— 叶子浓绿到发黑
- 秋 → autumn
- 深秋 → late autumn　— 落叶铺满地面
- 冬 → winter
- 初冬 → early winter　— 树枝光秃，地面有薄霜
- 隆冬 → deep winter　— 大雪把一切轮廓都抹平
- 梅雨 → the rainy season　— 初夏连续阴雨，一切湿透、绿色浓

> C · 场景

### 自然场景（5）

- 海边日落 → a purple sunset at the beach
- 火山喷发 → volcanic eruption　— 岩浆和火山灰从火山口喷出，天空被染红
- 沙漠绿洲 → a desert oasis　— 沙漠里的一小片水与植物，四周全是沙
- 浮岛群 → a cluster of floating islands　— 几块陆地悬在空中
- 杂草丛生的自然 → overgrown nature　— 植物把人工结构吃掉

### 奇幻场景（30）

- 魔法森林 → a magical forest
- 黑暗森林 → a dark forest
- 鬼屋森林 → a haunted forest
- 蘑菇森林 → a mushroom forest
- 魔法花园 → an enchanted garden
- 神秘山脉 → mystic mountains
- 仙人掌沙漠 → a cactus desert
- 水晶洞穴 → a crystal cave
- 天空岛屿 → a sky island
- 浮空城市 → a floating city
- 巴比伦空中花园 → the Hanging Gardens of Babylon
- 未来公园 → a futuristic park
- 冰雪王国 → an ice kingdom
- 热带天堂 → a tropical paradise
- 外星球 → an alien planet
- 月球地貌 → a lunar landscape
- 月球殖民地 → a lunar colony
- 在外太空 → outer space
- 虫洞 → a wormhole
- 反乌托邦未来 → a dystopian future
- 后启示录荒野 → a post-apocalyptic wasteland
- 蒸汽朋克工厂 → a steampunk factory
- 机器人工厂 → a robot factory
- 巨大机器 → giant machines
- 宇宙飞船 → a spaceship
- 废弃宇宙飞船 → an abandoned spaceship
- 赛博朋克小巷 → a cyberpunk alley
- 神话世界 → a mythical world
- 超现实梦境 → a surreal dreamscape
- 数字宇宙 → a digital universe

## 建筑空间

> A · 城市与建筑

### 城市景观（26）

- 城市 → city
- 街道 → street
- 老城区 → an old quarter with worn walls and tangled wires　— 墙面旧、电线乱拉
- 商业街 → a shopping street lined with signs　— 招牌一路铺过去
- 夜市 → a night market　— 摊位的灯把地面照成暖色
- 广场 → a plaza　— 空旷、铺装是几何的
- 小镇 → a small town　— 屋顶连成一片、街道很窄
- 浪漫小镇 → a romantic town
- 奇幻村庄 → a fantasy village
- 古罗马街道 → an ancient Roman street
- 港口 → a port with containers and cranes in rows　— 集装箱和吊机排成阵
- 近未来都市 → a near-future city
- 未来都市 → a futuristic metropolis
- 工业城市 → an industrial cityscape
- 霓虹城市 → a neon city
- 雨天城市 → a rainy city
- 赛博朋克城市 → a cyberpunk city
- 蒸汽朋克城市 → a steampunk cityscape
- 世界末日城市 → an apocalyptic city
- 废墟 → ruins
- 废弃城市建筑群 → deserted city buildings
- 古代遗迹 → ancient ruins
- 沉船遗迹 → a sunken shipwreck
- 冥界 → an underworld of dark structures and mist　— 成片的暗色建筑与雾
- 紫禁城 → the Forbidden City
- 赛博朋克丛林 → a cyber jungle

### 建筑类型（14）

- 摩天楼 → a skyscraper with a glass facade rising　— 玻璃的立面一直往上
- 塔 → a tower tapering as it rises　— 越往上越细
- 桥 → a bridge　— 墩子立在水中、拉索张开
- 图书馆 → a library　— 方正、开窗很少
- 灯塔 → a lighthouse
- 民居 → a vernacular house with a pitched roof and plain walls　— 坡屋顶、墙是素的
- 寺庙 → a temple
- 古代神庙 → an ancient temple
- 神秘古墓 → a mysterious tomb
- 水晶宫殿 → a crystal palace
- 魔法城堡 → a magical castle
- 中世纪城堡 → a medieval castle
- 童话城堡 → a fairy-tale castle
- 魔法王国 → a magical kingdom

> B · 室内

### 室内空间（23）

- 室内 → indoors
- 宫廷 → a palace interior
- 教堂 → a church
- 哥特式大教堂 → a Gothic cathedral
- 寺庙内 → a temple interior
- 温泉 → an onsen
- 酒吧 → a bar
- 居酒屋 → an izakaya
- 咖啡厅 → a cafe
- 教室 → a classroom
- 餐厅 → a restaurant
- 商店 → a shop
- 卧室 → a bedroom
- 厨房 → a kitchen　— 台面干净、器具有序
- 书房 → a study with books stacked to the ceiling　— 书一直堆到天花板
- 画廊 → a gallery　— 白墙、射灯只打作品
- 地铁车厢 → a subway car　— 扶手和吊环排成一列
- 体育馆 → an arena with tiers of seating rising　— 看台一圈圈围上去
- 舞台 → a stage
- 舞台灯光穿过烟雾 → stage beams cutting through haze　— 舞台烟机配聚光灯，光路明显，演出感
- 炼金室 → an alchemy laboratory
- 未来实验室 → a futuristic laboratory
- 黑暗地牢 → a dungeon

> C · 构件与做法

### 结构构件（28）

- 柱廊 → a colonnade of evenly spaced columns　— 等距排列的柱子撑起一条廊，古典建筑的常见做法
- 连续的拱券 → a run of arches receding one after another　— 罗马式与伊斯兰建筑
- 肋架拱顶 → ribbed vaulting with ribs crossing overhead　— 哥特式
- 外露的钢桁架 → exposed steel trusses with diagonal bracing　— 工业风
- 大跨度悬挑 → a long cantilever with nothing under it　— 结构只有一端固定，另一端凭空悬出
- 玻璃幕墙 → a full glass curtain wall　— 现代高层的外墙整面用玻璃，会反射天空和对面楼
- 天窗 → a skylight dropping light from the ridge　— 屋顶开的洞，把光从正上方引进来
- 老虎窗 → a dormer poking out of the pitched roof　— 斜屋顶上凸出的小窗，为阁楼采光
- 旋转楼梯 → a spiral stair winding around a central column　— 台阶围绕中心柱螺旋上升
- 女儿墙 → a low parapet along the roof edge　— 屋顶四周的安全矮墙
- 木格栅 → a timber louvre slicing light into stripes　— 细木条排成一排，光透过来变成一条条
- 飞檐翘角 → upturned eaves sweeping outward and up　— 中式与东亚建筑
- 斗拱层叠 → stacked dougong brackets stepping out　— 中式木构的承重构件
- 悬山顶 → an overhanging gable roof　— 中国古建筑屋顶等级最低的一种
- 歇山顶 → a hip-and-gable roof　— 一条正脊、四条垂脊、四条戗脊，共九脊
- 马头墙 → stepped gable walls rising above the roof　— 徽派建筑的山墙做成阶梯状高出屋顶（也叫封火墙）
- 月洞门 → a moon gate　— 中式园林的圆形门洞，本身就是一个取景框
- 影壁 → a free-standing screen wall facing the entrance　— 进门正对的一堵墙，挡住视线
- 美人靠 → a curved wooden bench along the veranda　— 江南园林里带靠背弧度的长凳
- 夯土墙 → rammed earth with horizontal lift lines　— 把土一层层夯实成墙，横向的层纹是施工痕迹
- 木模板木纹印在混凝土上 → timber grain left in the concrete　— 木纹被印在混凝土上
- 石材干挂 → dry-hung stone with straight joints　— 石板用金属件挂在墙上，板缝笔直且深
- 拉毛墙面 → a rough stucco wall like sandpaper　— 表面故意做成粗糙颗粒
- 老砖墙 → old brickwork with moss in the joints　— 旧砖墙，砖缝积了土长出青苔
- 水磨石 → terrazzo with chips set into cement　— 石子拌进水泥再磨平抛光
- 陶土砖 → terracotta brick　— 烧制时温度不匀，颜色深浅不一、有斑点
- 青瓷 → celadon　— 中国青瓷的釉色，粉青或梅子青，温润有玉感
- 悬索结构 → a cable-net roof　— 用钢索把屋顶吊起来，像吊桥一样

## 产品静物

> A · 构图与摆放

### 摆放方式（24）

- 产品居中 → product centred and fully visible　— 棚拍底盘写法
- 产品只占一角 → the product in one corner　— 大面积留白给文案
- 产品放在画面右侧 → the product on the right　— 官网首屏，留白给后期排版
- 产品占画面约六成 → the product fills about 60% of the frame　— 社媒方形图
- 产品斜靠 → the product leaning into a diagonal　— 形成一条对角线
- 产品悬浮在简洁背景中 → product floating in a clean background　— 科技／美妆／饮品广告
- 产品和包装同框 → the product in front of its packaging　— 层次清楚，适合礼盒与套装
- 产品与倒影同框 → the product with its reflection filling the lower half　— 倒影占下半格
- 产品被手拿着 → the product held in hand　— 只露手指
- 多个产品堆叠成塔 → products stacked into a tower
- 同系列产品排成一行 → the rest of the range blurred behind　— 虚化在后面
- 周围有少量相关道具 → a few relevant props that do not steal focus　— 但不抢主体
- 与产品同色的道具 → a prop in the same colour as the product　— 颜色呼应
- 一块有纹理的石板当台面 → a textured stone slab as the surface
- 一块垂落的丝绸 → silk falling in flowing folds　— 做出流动的褶
- 亚麻布做底 → a linen base with natural creases　— 有自然的褶
- 几何石膏块垫出层次 → geometric plaster blocks for depth
- 亚克力透明支架把产品垫高 → a clear acrylic riser lifting the product
- 一片干净的玻璃板做反射 → a clean glass sheet for reflection
- 细砂或小石子铺一层 → a bed of fine sand or pebbles
- 飘在空中的水花或粉末 → water or powder suspended in the air　— 悬浮感
- 干花或枝叶从边缘露进来 → dried leaves peeking in at the edge　— 只从边缘露进来
- 香水瓶 → a perfume bottle
- 化妆品瓶 → a cosmetic bottle

> B · 背景与台面

### 台面背景（10）

- 浅色台面 → a light-colored surface
- 浅灰棚拍背景 → light grey studio backdrop　— 影棚里用的浅灰背景纸，干净、不抢主体
- 无缝背景纸 → a seamless backdrop　— 背景纸从底部的浅灰渐变到顶部的白
- 纯白无缝背景（白底图） → seamless pure white, a cutout-ready backdrop
- 纯黑背景 → pure black with only the product edge lit　— 只留产品边缘的光
- 渐变背景 → a gradient darkening outward from the center　— 从中心往外变暗
- 几何色块背景 → geometric color blocks contrasting with the product　— 与产品形成对比
- 水波纹台面 → a rippled surface breaking up the reflection　— 倒影被拉碎
- 大理石台面，冷色调 → a cool-toned marble counter
- 与水同色的亚克力缸 → an acrylic tank　— 产品半浸

> C · 光效

### 光效（10）

- 大面积柔光箱在正上方，光很匀 → a large softbox directly overhead, very even
- 两侧各一块柔光板 → soft panels both sides leaving a vertical highlight　— 圆柱形产品用
- 顶部条光 → a strip light pulling one long highlight　— 在瓶身上拉出一条长高光
- 底光从亚克力台面透上来 → light coming up through an acrylic base
- 柔光加一块反光板补暗部 → soft key with a bounce filling the shadows
- 硬光加黑卡挡出明确的明暗交界 → hard light with black cards cutting the edge
- 聚光灯打出一小块圆斑 → a spotlight throwing one small pool
- 侧逆光勾出产品轮廓 → a rim of backlight tracing the silhouette
- 背光加柔和反射 → backlight with soft reflections to bring out transparency　— 玻璃杯／香水／护肤瓶／亚克力
- 高质感商业灯光配清晰阴影 → high-end commercial lighting with defined shadows

> D · 保真要求

### 保真要求（14）

- 保持产品的真实形状和材质 → keep the product's true shape and material　— ⭐ 产品图必写：不写模型会改形
- 保持产品原有形状、颜色和标签不变 → keep the product's original shape, colour and label unchanged
- 不要改变产品的结构、颜色和材质 → do not change the product's structure, colour or material
- 不要改变产品的比例和体积感 → do not change the proportions or volume
- 不要让产品弯曲或变形 → do not bend or distort the product
- 不要添加原产品没有的部件 → do not add parts the product does not have
- 材质要符合实物（哑光不要拍成亮面） → the finish must match reality
- 产品标签朝前 → the label faces the camera and stays readable　— 清晰可读
- 标志的位置与朝向保持不变 → keep the logo position and orientation
- 包装上的文字保持原样 → keep the packaging text exactly as it is　— 不要改写
- 颜色以参考图为准 → match the colour to the reference　— 不要偏色
- 保持参考图里的配色不变 → keep the reference palette
- 背景与产品同色系 → same hue behind　— 只靠明度拉开
- 主色取自品牌色 → primary colour taken from the brand palette

## 食物饮品

> A · 摆盘与餐具

### 摆盘（13）

- 主菜在中心 → the main centered　— 配菜围着摆一圈
- 用负空间把食物挤到一边 → negative space pushing the food to one side
- 桌面上留大片空白 → lots of empty table　— 食物只占一角
- 俯拍（餐具围成一圈） → top-down with cutlery circling the frame edge　— 餐具沿画面边缘排成圈
- 四十五度角或正俯拍 → a 45-degree or straight top-down angle　— 两个习惯角度，选一个
- 酱汁在盘底画一道弧 → a single arc of sauce across the plate　— 用勺背在盘底拖出一道弧线
- 只在食物上撒几粒盐和一点香草 → a few salt flakes and a sprig of herbs
- 少量配菜道具 → a few garnish props that do not steal focus　— 不抢主体
- 刀叉斜放在盘子外侧 → cutlery set at an angle outside the plate
- 掰开一半露出内里 → one half broken open to show the inside　— 展示切面和内馅
- 饮品杯壁上有冷凝水 → condensation on the glass　— 旁边散几块冰
- 冰镇过的杯壁起雾 → a chilled glass fogged with condensation
- 手正伸进画面 → a hand just entering the frame

### 食物质感（9）

- 食物新鲜真实 → food that looks fresh and real　— 有自然的油光
- 面包外壳脆硬 → a hard crust with strands pulling apart　— 欧包的外壳硬脆，掰开时内部有拉丝
- 焦褐色的边 → charred at the edges　— 表面煎到焦褐（美拉德反应），切开中间还是嫩的
- 焦糖化表面 → a caramelized top with a glossy crust　— 脆壳反光
- 酱汁浓稠 → a thick sauce coating the back of a spoon　— 挂得住勺背
- 汤汁表面有一层油光 → a sheen of fat on the surface of the broth
- 拉丝的奶酪 → melted cheese still strung　— 丝还连着
- 冰激凌边缘开始化 → ice cream just starting to melt　— 挂着水珠
- 切面清晰 → the cut surface is crisp　— 汉堡／蛋糕／水果类

### 餐具（11）

- 素白瓷盘 → a plain white porcelain plate　— 没有花纹
- 粗陶碗 → a rustic bowl with uneven glaze　— 釉面不均匀
- 原木托盘 → a raw wood tray with visible grain　— 木纹清楚
- 亚麻餐巾 → a linen napkin draped beside the plate　— 随意搭在盘子边上
- 铜锅 → a copper pot catching warm light on its walls　— 锅壁反着暖光
- 薄玻璃杯 → thin glass showing the colour behind it　— 杯壁透出对面的颜色
- 深色石板当盘子用 → a dark slate slab used as a plate
- 竹蒸笼 → a bamboo steamer just opened　— 盖子掀开还在冒气
- 旧砧板 → a worn board covered in knife marks　— 刀痕累累
- 一双漆筷 → lacquered chopsticks resting on a holder　— 架在筷托上
- 银质刀叉 → polished silver cutlery　— 反光很亮

> B · 光线与氛围

### 光线（7）

- 侧逆光 → back-side light glowing through the edges　— 食物的边缘被照透
- 顶部柔光加一块反光板补暗部 → a soft top light with a bounce card
- 窗边的自然光 → window light raking in from the front left　— 从左前方斜进来
- 深色背景配单侧光 → a dark ground with single-side light　— 主体像浮在暗处
- 逆光穿过半透明的食物 → backlight passing through translucent food
- 蒸汽被逆光照亮成一条条白线 → steam lit from behind into white threads
- 冷光加冰霜感 → cold light with condensation beading the glass　— 杯壁结着水珠

### 氛围（6）

- 干净的餐桌 → a clean dining table with natural light　— 光线自然
- 桌布有自然的褶皱 → a creased tablecloth with a fork beside　— 旁边放着一把叉子
- 木质桌面 → a wooden table with a dulled sheen　— 有一层用旧的暗哑光泽
- 背景是虚化的厨房 → a blurred kitchen behind　— 能看见一点热气
- 晨光从百叶窗斜切进来 → morning light cut into strips by blinds　— 一道一道
- 深色亚麻布 → dark linen with one pool of light on the food　— 只留一束光在食物上

## 抽象概念

> A · 形态

### 抽象形态（27）

- 流动的色块 → flowing color fields with soft edges　— 大片颜色互相渗透，没有明确边界
- 大面积渐变色域 → a large gradient field with no hard edge　— 整片区域是渐变，没有硬边
- 流体渐变 → an iridescent fluid gradient　— 颜色像油膜一样流动，带虹彩
- 液态金属 → liquid metal with a moving surface　— 像水银一样，表面一直在缓慢流动
- 粒子云 → a particle cloud thinning outward from the center　— 一堆粒子聚成云，中心最密、往外越稀
- 烟雾缠绕 → coiling smoke that never holds a shape　— 烟在空气里缠绕变形，没有固定形状
- 光的碎片 → shards of light scattering like broken glass　— 光被切成一块块碎片向外飞散
- 破碎的镜面 → a shattered mirror　— 镜子碎成很多块，每一块反射的角度都不同
- 水晶棱镜 → a crystal prism splitting light into bands　— 光穿过棱镜被分成几条不同颜色的光
- 线条相互交织成网 → lines interlacing into a mesh　— 很多线互相穿插，织成一张网
- 涟漪从中心一圈圈扩散 → ripples spreading ring by ring from the center　— 水面被打一下，波纹一圈圈往外推
- 同心圆扩散 → concentric circles radiating out　— 从中心一圈圈往外放的圆，视线被拉向圆心
- 一道贯穿画面的斜线 → a single diagonal cutting across the frame
- 细密噪点与颗粒覆盖整张图 → fine noise and grain over the whole frame　— 细小的噪点铺满画面，像胶片颗粒
- 分形 → fractal
- 分形结构，自相似 → a self-similar fractal structure　— 放大后每一小块都和整体长得一样
- 斐波那契数列 → Fibonacci
- 黄金螺旋 → a golden spiral　— 按黄金比例一圈圈放大的螺旋
- 等距立方体堆叠 → stacked isometric cubes　— 等距视角下把立方体叠起来
- 圆形与六边形网格叠加 → overlapping circles over a hexagonal grid　— 两种网格叠在一起，产生干涉感
- 立方体堆叠成不规则的山 → cubes stacked into an irregular mass　— 大小不一的立方体堆出一座不规则的体块山
- 电子电路 → electronic circuitry
- 坐标网格与刻度线 → a coordinate grid with tick marks　— 带刻度的网格，像坐标纸
- 单向箭头 → a single directional arrow
- 无限循环的箭头 → a looping infinity arrow　— 首尾相接的箭头，表示循环
- 十字准星 → a crosshair　— 交叉的细线，像瞄准镜
- 三个同心圆组成的靶心 → a bullseye of three concentric rings

### 几何（12）

- 球体 → a sphere with an even matte surface　— 表面是均匀的哑光
- 多面体 → a polyhedron with every face catching light　— 由多个平面组成的立体，每个面反光方向都不同
- 四棱锥 → a pyramid with hard edges　— 底面是四边形的锥体，棱线锐利
- 球面网格 → a sphere wrapped in a latitude-longitude grid　— 像地球仪那样用经纬线包住球
- 莫比乌斯环 → a Möbius strip with a single surface　— 把纸带拧半圈接上，只有一个面、一条边
- 剪影 → silhouette　— 背景亮、主体全黑，只剩一个轮廓，看不出五官
- 印刷网点 → halftone dots　— 网点从大到小排列，远看是一个渐变
- 圆点阵列 → a dot field fading from dense to sparse　— 点阵从密到疏渐变，形成方向的暗示
- 虚线框 → a dashed box marking out a region　— 用虚线画出范围，提示这块是要强调的
- 编号标签 → numbered callout tags　— 带数字的小标签加引线，像工程图纸上的标注
- 一个对勾 → a check mark　— 明确表示肯定
- 一个叉号 → a cross mark　— 明确表示否定

> B · 纹样

### 纹样（15）

- 曼陀罗 → mandala　— 从中心向外对称展开的圆形图案，源自佛教坛城
- 祥云纹 → auspicious cloud pattern　— 中国传统吉祥纹样，云头卷曲成套
- 回纹边框 → meander border pattern　— 由连续方形回折组成的边框纹
- 鱼鳞纹 → a fish-scale pattern　— 像鱼鳞一样层层叠压的半圆排列
- 碎裂纹 → crackle glaze　— 不规则的裂纹遍布表面，像冰裂或瓷器开片
- 花卉纹样 → floral pattern
- 宽条纹 → wide vertical stripes at even spacing　— 等宽等距的竖条
- 细格纹 → a fine check　— 细密的方格，像衬衫布
- 千鸟格 → houndstooth　— 由小方块拼成的锯齿状格纹
- 波尔卡圆点 → polka dots　— 均匀排布的小圆点
- 豹纹 → leopard spots
- 斑马纹 → zebra stripes　— 黑白相间
- 大理石纹 → marble veining that forks naturally　— 石头的纹路自然分叉延伸，没有规律
- 水磨石纹 → terrazzo with stones of mixed size　— 满地小石子嵌在底色里，大小颜色都不同
- 洛阳花石纹 → Luoyang flower-and-stone pattern

## 文字平面

> A · 图表与信息元件

### 信息图元件（23）

- 技术画 → a technical drawing with annotations　— 像工程图纸一样标注
- 蓝图 → blueprint　— 蓝底白线的制图
- 线框图 → a wireframe drawing
- 剖面图 → a cutaway
- 爆炸图 → an exploded view　— 零件沿轴线拉开
- 户型图 → a floor plan seen from directly above　— 从正上方看平面布局
- 细线图表 → a thin-line chart with the data line only　— 只留数据线，去掉网格与边框
- 柱状图 → a bar chart with a shared baseline　— 柱子底部对齐
- 饼图 → a pie chart labeling only the largest slice　— 只标最大的一块
- 趋势图 → a trend illustration
- 时间轴 → a timeline with nodes on a single line　— 节点串在一条横线上
- 流程图 → a flowchart of boxes and arrows　— 方框加箭头
- 对比表格 → a two-column comparison table　— 两列并排
- 图标组 → an icon set with a consistent stroke width　— 统一线宽
- 进度条 → a progress bar with a clear filled remainder　— 填充与未填充对比清楚
- 圆角矩形标注框 → a rounded callout box with a leader line pointing to the subject　— 一条引线指向主体
- 三到五个彩色圆点当图例 → three to five coloured dots as a legend
- 一条粗横线当分区标题 → a thick horizontal rule acting as a section heading
- 数字用超大字号单独占一块 → the number set very large in its own block
- 关键数字放大到正文的三倍 → key figures set at triple body size
- 箭头连接前后两步 → an arrow connecting two steps
- 地图标注点 → a map pin with a leader line　— 带一条引线
- 半调网点做的明暗过渡 → a halftone dot gradient

> B · 排版与字体

### 版式（12）

- 正文只用宋体、黑体、楷体三种 → body text in serif　— 其他字体整段排会累
- 一页里最多两个中文字体家族 → at most two Chinese type families per page　— 加载与统一性双重考虑
- 字号档位不超过六档 → no more than six type sizes　— 档位多了层级贬值
- 字重从细到粗拉开档次 → full weight range from light to heavy　— 只有两档时层级全靠字号撑
- 大标题的字距收紧 → tight letter-spacing on large headings　— 大字号下空隙会被放大
- 正文行长收住 → line length capped around 30 characters　— 行长失控是可读性问题里排第一的
- 数字用等宽数位对齐 → tabular figures for numbers　— 数字宽度不等会让列左右抖动
- 竖排文字 → vertical writing　— 适合书脊式标题、诗词、目录
- 标题压在图上 → the title over the image on a darkened band　— 底下垫一层压暗
- 网格对齐 → everything snapped to one grid　— 所有元素贴同一条基线
- 信息密度低 → low density　— 留出大块呼吸空间
- 中英文混排 → mixed Chinese and Latin　— 英文用小一号的字重

### 字体（10）

- 思源黑体 → Noto Sans SC　— 免费商用(OFL)；当默认正文不会错
- 思源宋体 → Noto Serif SC　— 免费商用(OFL)；Heavy 字重可当大标题
- 霞鹜文楷 → LXGW WenKai　— 免费商用(OFL)；适合文艺、教育、引言
- 霞鹜新晰黑 → LXGW Neo XiHei　— 免费商用
- 汇文明朝体 → Huiwen Mingchao　— 免费商用；适合书封、文化类
- 京华老宋体 → Jinghua Old Song　— 免费商用；标题专用
- 源流明体 → GenRyuMin　— 免费商用(OFL)；繁体内容首选
- 未来荧黑 → Glow Sans　— 免费商用(OFL)；压缩宽度可做窄长大标题
- MiSans → MiSans　— 免费商用；界面原型合适
- 得意黑 → Smiley Sans　— 免费商用(OFL)；标题专用，正文用会晕

> C · 海报与规格

### 海报元素（6）

- 顶部标题、中心主体、底部信息区 → title on top, subject in the centre, information block at the bottom　— ⭐ 最稳的海报层级配方
- 大标题加一行副标题 → a large headline with one line of subheading
- 三个卖点标签 → three selling-point tags　— 课程／产品海报
- 底部保留价格和按钮区域 → leave room for price and button　— 电商促销；具体数字交给后期
- 主体占画面约五成半 → the subject fills about 55% of the frame　— 信息流广告
- 画面里只出现引号内的文字 → only the text inside the quotation marks appears in the image　— ⭐ 控制图中文字最有效的一句

### 平台规格（5）

- 竖版图文笔记 → vertical image post　— 1080×1440，三比四
- 图文笔记一套 → a set of 1 cover + 4-8 content pages + 1 summary page
- 自媒体封面主图 → article cover　— 标题放在中偏左的清晰安全带里，避免中间发空
- 自媒体方形封面 → square cover　— 默认只放短标题、大字居中，不放图
- 方图里的短标题压到四到十个字 → keep the square-cover title to 4-10 characters　— 不要把横版长标题硬塞进方图
