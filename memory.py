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
    def __init_(self):
        pass

    def get(self, value):
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
            to_return = self.__dict__[value]

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
        setattr(obj, var, value)

    def print_dict(self):
        pprint.pprint(full_vars(self))