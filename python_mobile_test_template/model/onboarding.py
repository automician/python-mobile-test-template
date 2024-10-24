from selene.support._mobile import device


class Onboarding:
    Skip = device.element('fragment_onboarding_skip_button')
    Continue = device.element('fragment_onboarding_forward_button')
