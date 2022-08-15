from pyodide import create_proxy
from js import clearInterval, setInterval, console
from typing import Tuple

class moving_element():
    def __init__(self, element, container, event: str, interval_delay: int, x_range: Tuple[int, int], y_range: Tuple[int, int]) -> None:
        self.element = element
        self.container = container
        self.x_range = x_range
        self.y_range = y_range
        self.event = event
        self.interval_delay = interval_delay
        
        self.id = None
        self.cur_x = self.x_range[0]
        self.cur_y = self.y_range[0]
        self.has_moved = False  # Has the element responded to an event yet?
        
        # First, set up the event listener for the element.
        container.element.addEventListener(self.event, create_proxy(self.event_responder))
        
        console.log(f'{self} created')
        
    def event_responder(self, event) -> None:
        """
        This function is called when the event is triggered.
        """
        console.log(f'{self} triggered {self.event}')
        self.has_moved = not self.has_moved
        clearInterval(self.id)
        self.id = setInterval(create_proxy(self.move), self.interval_delay)
        
    def move(self) -> None:
        """
        This function is called every interval_delay milliseconds.
        """
        
        if self.has_moved:
            if self.cur_x == self.x_range[1] and self.cur_y == self.y_range[1]:
                clearInterval(id)
            else:
                self.cur_x += 1
                self.cur_y += 1
                
                # Make sure not to go out of the given range.
                if self.cur_x > self.x_range[1]:
                    self.cur_x = self.x_range[1]
                
                if self.cur_y > self.y_range[1]:
                    self.cur_y = self.y_range[1]
                    
                self.element.element.style.left = str(self.cur_x) + 'px'
                self.element.element.style.top = str(self.cur_y) + 'px'
            
        else:
            if self.cur_x == self.x_range[0] and self.cur_y == self.y_range[0]:
                clearInterval(id)
            else:
                self.cur_x -= 1
                self.cur_y -= 1
                
                # Make sure not to go out of the given range.
                if self.cur_x < self.x_range[0]:
                    self.cur_x = self.x_range[0]
                
                if self.cur_y < self.y_range[0]:
                    self.cur_y = self.y_range[0]
                    
                self.element.element.style.left = str(self.cur_x) + 'px'
                self.element.element.style.top = str(self.cur_y) + 'px'
                
    def __repr__(self) -> str:
        return f'{self.element}: ({self.cur_x}, {self.cur_y})'