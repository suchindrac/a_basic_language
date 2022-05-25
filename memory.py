from link import Link
import pprint


def full_vars(obj):
    return {k: full_vars(v) if hasattr(v, '__dict__') else v for k, v in vars(obj).items()}

def get_nested_keys(d, keys):
    for k, v in d.items():
        if isinstance(v, dict):
            keys.append(k)
            get_nested_keys(v, keys)
        else:
            keys.append(k)


class Memory:
    orig_memory = None
    def __init_(self):
        self.eresult = None
        Memory.orig_memory = self

    def get(self, value):
        if value.isdigit():
            return int(value)

        all_vars = full_vars(self)

        if "." in value:
            mod = value.split(".")[-1]
        else:
            mod = value
        
        keys_list = []
        get_nested_keys(all_vars, keys_list)
        
        if mod not in keys_list:
            return False

        if "." in value:
            vlist = value.split(".")
            mod = vlist.pop()

            dct = all_vars
            
            for i in range(len(vlist)):
                dct = dct[vlist[i]]

            to_return = dct[mod]
        else:
            if mod in self.__dict__.keys():
                to_return = self.__dict__[mod]
            else:
                to_return = False
                for value in self.__dict__.values():
                    
                    if isinstance(value, Memory):
                        if mod in value.__dict__.keys():
                            to_return = value.__dict__[mod]
                            break
                
        return to_return

    def get_obj(self, var):
        vlist = var.split(".")
        cur_obj = self
        for i in range(len(vlist)-1):
            cur_obj = getattr(cur_obj, vlist[i])
        
        return cur_obj

    def set(self, var, value):
        obj = self.get_obj(var)
        var = var.split(".")[-1]

        if isinstance(value, str):
            if self.get(value):
                value = self.get(value)

        setattr(obj, var, value)

    def print_dict(self):
        pprint.pprint(full_vars(self))

mem_local = Memory()
