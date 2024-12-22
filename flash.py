from flet import *


def system(page:Page):
    
    page.title = 'إضاءة كشاف'
    page.window.color = colors.SILVER
    page.window.height = 742
    page.window.width = 392
    page.window.top = 12
    page.scroll = 'auto'
    page.theme_mode = ThemeMode.LIGHT
    
    
    flash = FlashLight()
    options = PermissionHandler()
    
    def setting(x):
       options.open_app_settings()
       
       
       
    page.overlay.appenx(options)
    page.overlay.append(flash)
    
    bar1 = AppBar(
           title = text('إضاءة كشاف'),
           bgcolor = colors.ORANGE,
           color = colors.BLACK,
           center_title = True,
           
           leading = Icon(Icons.NOTIFICATIONS),
           leading_width = 42,
           
           actions = [
           
              IconButton(icons.SETTINGS , on_click = settings)
           ]
    ),
    
    row1 = Row([
          Text('\n\n إضاءة كشاف' , size = 32 , color = 'black' )
          ] , alignment = MainAxisAlignment.CENTER)
          
    row2 = Row([
          Image(src = '' , width = 362)
          ] , alignment = MainAxisAlignment.CENTER)
    
    row3 = Row([
          
          ElevatedButton(
              'ON',
              width = 102,
              icon = icons.PLAY_ARROW,
              style = ButtonStyle(
                     bgcolor = '#e3ll3e',
                     color = colors.BLACK,
                     padding = 16,
                     shape = ContinuesRectangleBorder(radius = 102)
                     
               ) , on_click = lambda x: flash.turn_on
          ),
          
          ElevatedButton(
              'OFF',
              width = 102,
              icon = icons.PLAY_DISABLED_SHARP,
              style = ButtonStyle(
                     bgcolor = '#e3ll3e',
                     color = colors.BLACK,
                     padding = 16,
                     shape = ContinuesRectangleBorder(radius = 102)
                     
               ) , on_click = lambda x: flash.turn_off
          )
          
          
          
          
          
          ] , alignment = MainAxisAlignment.CENTER)
          
     
    
    page.add(bar1 , row1 , row2 , row3)
    page.update()
  
app(system)
    